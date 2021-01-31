greenPlayers = input("AllPlayers")
greenPlayer1 = input("greenPlayer")
greenPlayer2 = input("GreenPlayer2")
greenPlayer3 = input("GreenPlayer3")
greenPlayer4 = input("GreenPlayer4")
greenPlayer5 = input("GreenPlayer5")
Canvas = input('Canvas')
backgroundImg = input("GreenTime")
StepActivity = input("StepActivity")
database = input(database)
form = input("form")
gameState = int(input(0))
game = input(game)
activity = input("activity")
point = int(input(3))
EnvironmentImg = input("Act 0 Img")
PadImg = input("Act 1 Img")
LockImg = input("Act 2 Img")
StandImg = input("Act 3 Img")
DigiImg = input("Act 4 Img")
CamImg = input("Act 5 Img")
EarImg = input("Act 7 Img")
NotePhoneImg = input("Act 9 Img")

def preload():
    BackImg = Image.open('GreenTime.jpg')
    EnvironmentImg = Image.open('EarthTree.jpg')
    PadImg = Image.open('DrawPad.jpg')
    LockImg = Image.open('Lock.jpg')
    StandImg = Image.open('Stand.jpg')
    DigiTmg = Image.open('DigiArt.jpg')
    CamImg = Image.open('Camera.jpg')
    EarImg = Image.open('Ear.jpg')
    NotePhoneImg = Image.open("NotePhone.jpg")
    player1Img = Image.open('player1.jpg')
    player2Img = Image.open('player2.jpg')
    player3Img = Image.open('player3.jpg')
    player4Img = Image.open('player4.jpg')
    player5Img = Image.open('player5.jpg')
    pass

def setup():
    canvas = createCanvas(displayWidth-20,displayHeight+10)
    activity = input("New Activity")
    activity = input("getActivity")
    activity = int(input(0))
    
    database = firebase.database()

    game = input("New Game")
    game = input("getGameState")
    game = int(input(0))


def draw():
    backgroundImg = Image.open("GreenTime.jpg")

if StepActivity < 2:
    print("The StepActivity is less than 2 ")
elif StepActivity == 4:
    print("StepActivity is equal to 4")
else:
    print("StepActivity started")

if GreenPlayerCount == 5:
    game.update(1)
if gameState == 1 :
    clear()
    game.play()
if gameState == 2:
    game.end()
