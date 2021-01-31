class Game:
    def _init_(this,gameState):
        this.gameState = str(input(0))
        pass

    def getState():
        this_gameStateRef = database.ref('gameState')
        this_gameStateRef.on("value",(data))
        this.gameState = data.value()

    def update(gameState):
        database.ref('/').update
        gameState = state

    def  start():
        if(gameState == 0):
            greenPlayer = input(GreenPlayer)
            this_GreenPlayerCountRef = database.ref('GreenPlayerCount').once("value")
        if(GreenPlayerCountRef.exist):
            GreenPlayerCount = GreenPlayerCountRef.val()
            GreenPlayer.getGreenPlayerCount()

        Form = input("Green Form")
        form.display()

        greenPlayer1 = createSprite(100,200)
        player1Img = Image.open('player1.jpg')
        greenPlayer2 = createSprite(300,200)
        player2Img = Image.open('player2.jpg')
        greenPlayer3 = createSprite(500,200)
        player3Img = Image.open('player3.jpg')
        greenPlayer4 = createSprite(700,200)
        player4Img = Image.open('player4.jpg')
        greenPlayer5 = createSprite(900,200)
        player5Img = Image.open('player5.jpg')
        greenPlayers = input([greenPlayer1, greenPlayer2, greenPlayer3, greenPlayer4,greenPlayer5])

       def  play():
        form.hide()

        greenPlayer.getPlayerInfo()
        
        if(allGreenPlayers != undefined):
            background(rgb(34,139,34))
            image(track,0,-displayHeight*4,displayWidth,displayHeight*5)

        #var display_position = 100;
      
      #index of the array
            Actindex = int(input(0))

      #x and y position of the players
       x = 175 
       y = 0

            for activity in (0,11):
                print(0,11)
       #add 1 to the index for every loop
            Actindex = Actindex + 1 

        #position the players a little away from each other in x direction
        x = x + 200
        #use data form the database to display the players in y direction
        y = displayHeight - allGreenPlayers[0,1,2,3,4,5].distance
        players[index-1].x = x
        players[index-1].y = y
        print(index, Act.index)

       
        if Actindex == Actindex:
          
          fill("red")
          players[index - 1].shapeColor = "red"
          camera.position.x = displayWidth/2
          camera.position.y = players[index-1].y
        
       
        textSize(15)
        text(Players[plr].name + ": " + Players[plr].point, 120,display_position)


        if keyIsDown(UP_ARROW) and player.index !== 0:
           greenPlayer.point +=3
           greenPlayer.update()

        if player.point > 33:
            gameState = 2
            greenPlayer.rank +=1

    def  end():
        print("Game Ended")
        print(greenPlayer.rank)








    
    
    
