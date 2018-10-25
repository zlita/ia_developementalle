import numpy as np


class Agent:
    ListFeed = []
    def __init__(self):
        self.actions = ["a1","a2"]
    def predict(self,actions):
        for i in self.ListFeed:
            if actions in i:
                return i[1]
        return None

class Env:
    def __init__(self):
        self.env1 = [["a1","f1"],["a2","f2"]]
        self.env2 = [["a1","f2"],["a2","f1"]]

    def feedback(self,env,action):
        if env == self.env1:
            if action == "a1":
                return "f1"
            if action == "a2":
                return "f2"
        if env == self.env2:
            if action == "a1":
                return "f2"
            if action == "a2":
                return "f1"


if __name__ == '__main__':

    n = 10
    agent = Agent()
    env = Env()

    for i in range(n):

        actions = agent.actions[0]
        print("Agent choisi une action : ",actions)
        predict = agent.predict(actions)
        print("L'agent prédit : ",predict)


        print("Action est : ",actions)
        f1 = env.feedback(env.env1, actions)
        print("Feedback obtenu : ", f1)
        if predict == f1:
            print("Je suis content !")
        else:
            print("Hmm... Ca ne va pas du tout !")
            if not predict == None:
                agent.ListFeed.remove([actions,predict])
            agent.ListFeed.append([actions,f1])
        print("")