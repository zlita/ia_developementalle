

class Agent:
    ListFeed = []

    def __init__(self):
        self.actions = ["a1","a2"]
        self.action = None
        self.predictions = None

    def predict(self,actions):
        for i in self.ListFeed:
            if actions in i:
                return i[1]
        return None

    def play(self):
        self.action = self.actions[0]
        print("Agent choisi une action : ",self.action)
        self.predictions = self.predict(self.action)
        print("L'agent prédit : ",self.predictions)

    def update(self,feedback):
        print("Feedback obtenu : ", feedback)
        if self.predictions == feedback:
            print("Je suis content !")
        else:
            print("Hmm... Ca ne va pas du tout !")
            if not self.predictions == None:
                agent.ListFeed.remove([self.action,self.predictions])
            agent.ListFeed.append([self.action,feedback])
        print("")

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

        agent.play()
        f1 = env.feedback(env.env1, agent.action)
        agent.update(f1)

