import core


class ScoreManager:

    def load(self, filename):

        f = open(filename, "r")

        for i in f:
            if i != "\n":
                core.memory("score").append(ScoreManager.ScoreList(i.split(":")[0], i.split(":")[1]))

    def write(self, filename):

        f = open(filename, "w")

        print(len(core.memory("score")))


        for i in core.memory("score"):

            f.write(i.pseudo + ":" + str(i.score) + "\n")

        f.close()

    def insert(self, ScoreList):

        j = 0
        for i in core.memory("score"):

            if (int(i.score) < ScoreList.score):

                core.memory("score").insert(j, ScoreList)

                break

            else: j+=1



    class ScoreList:
        def __init__(self, pseudo, score):
            self.pseudo = pseudo
            self.score = score