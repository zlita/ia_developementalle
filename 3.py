import numpy as np


class Agent:

    def __init__(self):
        self.actions = ["a1","a2"]
        self.ListFeed = []
        self.ListCouple = []
        self.value = None
        self.prediction = None
        self.action = None
        self.valAction = 0
        self.interactions_composite = []
        self.interaction_courante = []
        self.value_composite = 0


    def predict(self,actions) :
        for i in self.ListFeed:
            if actions in i:
                return i[1]
        return None


    def play(self):
        temp = self.activate_composite()
        update = False

        while temp != [] :
            if min(temp, key=lambda coll: len(coll))[-1] > 0 :     #si la valeur de l'interaction composite activé restante la plus petite est positive on poursuit son execution
                self.action = min(temp, key=lambda coll: len(coll))[1]
                update = True
                temp = []
            else :  #sinon on la supprime de temp pour tester les suivantes.
                del(temp[temp.index(min(temp, key=lambda coll: len(coll)))])    #revient a prendre la premiere interaction car elles sont toutes composé de 2 actions mais le code est générique.
        if not update :     #si on as pas d'interaction composite activé dont la valeur est positive.
            self.action = self.actions[self.valAction]
        print("Agent choisi une action : ",self.action)
        self.prediction = self.predict(self.action)
        print("L'agent prédit : ",self.prediction)
        return self.action


    def update(self, feedback):
        self.value = val.get_value(a, feedback)
        print("Feedback obtenu : ", feedback)
        print("Valeur obtenu : ",self.value)
        if self.prediction == feedback:
            print("Je suis content car j'ai bien prédit !")

            if self.value > 0:
                print("Positif parfait !")
                varCouple = (self.action + feedback, self.value)
                if varCouple not in self.ListCouple:
                    self.ListCouple.append(varCouple)
            else:
                print("Mince, c'est négatif :(")
                self.valAction = (self.valAction + 1) % 2
        else:
            print("Hmm... Ca ne va pas du tout je n'ai pas bien prédit mon feedback !")
            if not self.prediction == None:
                self.ListFeed.remove([self.action,self.prediction])
            self.ListFeed.append([self.action,feedback])
            if self.value > 0:
                print("Positif parfait !")
                varCouple = (self.action + feedback, self.value)
                if varCouple not in self.ListCouple:
                    self.ListCouple.append(varCouple)
            else:
                print("Mince, c'est négatif :(")
                self.valAction = (self.valAction + 1) % 2
                varCouple = (self.action + feedback, self.value)
                if varCouple not in self.ListCouple:
                    self.ListCouple.append(varCouple)
        #print("COUPLE",self.ListCouple)
        #print(self.ListFeed)
        #print("")

        #mis a jour des interactions.
        self.interaction_courante.append(self.action)
        self.value_composite += self.value
        if self.interaction_courante not in self.interactions_composite and len(self.interaction_courante) == 2 :   # remplacer le == par >= pour permettre des actions composite de taille arbitraire.
            self.interaction_courante.append(self.value_composite)
            self.interactions_composite.append(self.interaction_courante)
            self.value_composite = 0
            self.interaction_courante = [self.action]


    #retourne la ou les actions composite activé si il y en as.
    def activate_composite(self):
        A = []
        for i in self.interactions_composite :
            if i[0] == self.action :
                A.append(i)
        return A


class Env:
    def __init__(self, env):

        self.env1 = {"a1":"f1","a2":"f2"}
        self.env2 = {"a1":"f2","a2":"f1"}
        self.env = env
        self.nbPas = 0
        self.actionPrecedente = None


    def feedback(self, action):
        if self.env == 1:
            return self.env1.get(action)
        if self.env == 2:
            return self.env2.get(action)
        if self.env == 3:
            if self.nbPas < 5:
                self.nbPas += 1
                return self.env1.get(action)
            else:
                return self.env2.get(action)
        if self.env == 4:
            if self.actionPrecedente == action:
                self.actionPrecedente = action
                return "f1"
            else:
                self.actionPrecedente = action
                return "f2"




class Values:
    def __init__(self,val):
        if val == 1:
            self.val1 = {"a1f1":1,"a1f2":1,"a2f1":-1,"a2f2":-1}
        if val == 2:
            self.val2 = {"a1f1":-1,"a1f2":-1,"a2f1":1,"a2f2":1}
        if val == 3:
            self.val3 = {"a1f1":-1,"a2f1":-1,"a1f2":1,"a2f2":1}
        self.val = val


    def get_value(self,action,feedback):
        temp = action + feedback
        if self.val == 1:
            value = self.val1.get(temp)
        if self.val == 2:
            value = self.val2.get(temp)
        if self.val == 3:
            value = self.val3.get(temp)
        return value



if __name__ == '__main__':

    n = 10
    agent = Agent()
    env = Env(3)
    val = Values(2)
    for i in range(n):
        a = agent.play()
        f1 = env.feedback(agent.action)
        agent.update(f1)
        print("Action",i+1,a,f1,agent.value)
        print("\n\n")
