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
        env1 = 0

    def feedback(self):
        function1 = "f1"
        function2 = "f2"

def feedback(action):
    if action == "a1":
        return "f1"
    if action == "a2":
        return "f2"

if __name__ == '__main__':

    n = 10
    agent = Agent()

    for i in range(n):

        actions = agent.actions[0]
        print("Agent choisi une action : ",actions)
        predict = agent.predict(actions)
        print("L'agent prédit : ",predict)


        print("Action est : ",actions)
        f1 = feedback(actions)
        print("Feedback obtenu : ", f1)
        if predict == f1:
            print("YOUUUHOUUUU !")
        else:
            print("Mais euuuuuh :(")
            if not predict == None:
                agent.ListFeed.remove([actions,predict])
            agent.ListFeed.append([actions,f1])
        print("")