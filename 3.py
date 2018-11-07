import numpy as np


class Agent:

    def __init__(self):
        self.actions = ["a1","a2"]
        self.ListFeed = []
        self.ListCouple = [['None',-1],['None',-1]]
        self.AllCouple = {}
        self.value = None
        self.prediction = None
        self.action = None
        self.valAction = 0


    def predict(self, actions):
        for i in self.ListFeed:
            if actions in i:
                return i[1]
        return None

    def play(self):
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
                self.valAction += 1 % 2
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
        print("COUPLE",self.ListCouple)
        print(self.ListFeed)
        print("")
##################################################################################

    def agent_action(self):

        self.action = self.actions[self.valAction]
        return self.action

    def agent_predict(self):
        self.prediction

    def agent_valeur(self,feedback):
        #self.value = val.get_value(self.action,feedback)
        #if len(self.ListCouple) < 2:
        #    self.ListCouple.append([self.action+feedback,self.value])
        #else:
        self.ListCouple.pop(0)
        self.ListCouple.append([self.action,feedback])
        print("ListeCOUPLE :",self.ListCouple)

    def activate_composite(self):
        A = self.AllCouple.get(self.action)
        print("All couple starting with action",self.AllCouple.get(self.action))
        print("Activate composite",A)
        return A

    def interaction_set(self):
        couple = (self.ListCouple[0][0]+self.ListCouple[1][0])
        if couple not in self.AllCouple:
            self.AllCouple[couple] = f1

    def agent_maj(self,feedback):

        self.agent_valeur(feedback)
        self.interaction_set()
        A = self.activate_composite()
        print(self.ListCouple)
        if self.ListCouple[0][1] + self.ListCouple[1][1] < 0:
            self.valAction = (self.valAction + 1) % 2


#############################################################################




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
    env = Env(4)
    val = Values(3)
    for i in range(n):
        a = agent.agent_action()
        f1 = env.feedback(a)
        agent.agent_maj(f1)

