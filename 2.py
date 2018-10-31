import numpy as np


class Agent:

    def __init__(self):
        self.actions = ["a1","a2"]
        self.ListFeed = []
        self.prediction = None
        self.action = None


    def predict(self,actions) :
        for i in self.ListFeed:
            if actions in i:
                return i[1]
        return None


    def play(self):
        self.action = self.actions[0]
        print("Agent choisi une action : ",self.action)
        self.prediction = self.predict(self.action)
        print("L'agent prédit : ",self.prediction)
        return self.action

    def update(self, feedback):
        value = val.get_value(a, feedback)
        print("Feedback obtenu : ", feedback)
        print("Valeur obtenu : ",value)
        if self.prediction == feedback and value > 0:
            print("Je suis content !")
        else:
            print("Hmm... Ca ne va pas du tout !")
            if not self.prediction == None:
                self.ListFeed.remove([self.action,self.prediction,value])
            self.ListFeed.append([self.action,feedback,value])
        print(self.ListFeed)
        print("")




class Env:
    def __init__(self, env):
        if env == 1:
            self.env1 = [["a1","f1"],["a2","f2"]]
        if env == 2:
            self.env2 = [["a1","f2"],["a2","f1"]]
        self.env = env

    def feedback(self, action):
        if self.env == 1:
            if action == "a1":
                return "f1"
            if action == "a2":
                return "f2"
        if self.env == 2:
            if action == "a1":
                return "f2"
            if action == "a2":
                return "f1"

class Values:
    def __init__(self,val):
        if val == 1:
            self.val1 = {"a1f1":1,"a1f2":1,"a2f1":0,"a2f2":0}
        if val == 2:
            self.val2 = {"a1f1":-1,"a1f2":-1,"a2f1":1,"a2f2":1}
        if val == 3:
            self.val3 = {"a1f1":1,"a2f1":1,"a1f2":-1,"a2f2":-1}
        self.val = val

    def get_value(self,action,feedback):
        temp = action + feedback
        print("temp ",temp)
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
    env = Env(1)
    val = Values(3)
    for i in range(n):
            a = agent.play()
            f1 = env.feedback(agent.action)
            agent.update(f1)
