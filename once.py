
import yaml

file = open("game.yaml", "r")
game = yaml.load(file)
file.close()

### this function ask the question with name Q
def AskGame(Q):
  while True:
    print(game[Q]["text"])
    options = game[Q]["options"]
    for key, value in options.items() :
      print (key, value["choice"])
    c = input()
    choice = options[c]
    print(choice["outcome"])
    # print("suivant:", choice["next"])
    if(choice["next"] == "exit"):
      exit()
    AskGame(choice["next"])

AskGame("start")

