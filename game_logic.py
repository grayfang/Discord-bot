import random
import time
import scores

MAX_RANGE = 100

async def play_game(message, client, scores):
    playing = True
    gameover = False
    winner = False
    currentRand = MAX_RANGE
    username = "empty"
    turnCount = 0

    user1 = str(message.author).split('#')[0]
    user2 = ""
    scores[user1] = scores.get(user1, 0)

     #game loop
    while not gameover:
        # time to help deter the bot from reading it's own messages
        time.sleep(2)
        if currentRand != MAX_RANGE:
            message = await client.wait_for('message')
            #makes sure that the bot messages aren't being used
            if message.author == client.user:
                continue            

        
        # parses the username from the discord username
        name = str(message.author).split('#')
        # logic to create a new user
        if  name[0] != user1:
            user2 = name[0]
            scores[user2] = scores.get(user2, 0)
        # debug message
        # await message.channel.send(f'user1: {user1}\nname: {name[0]}\nturncount: {turnCount}')
        if (turnCount%2 == 0) and (user1 != name[0]):
            print("error")
            await message.channel.send("```You can't play twice in a row!```")
            continue
        elif((turnCount%2 == 1) and (user2 != name[0])):
            print("error")
            await message.channel.send("```You can't play twice in a row!```")
            continue  
        # debug message to track the id/username of the user who sent the message
        # await message.channel.send(f'name: {name[0]}\nuser1: {user1}')
        

        currentRand = random.randint(1, currentRand)
        print(f'doing rand of {currentRand}')

        if currentRand == 1:
            await message.channel.send(f'```{name[0]} rolled a 1 and lost.```')
            print(turnCount)

            #logic for 
            if turnCount%2 == 0:
                winner = True
            else:
                winner = False

            gameover = True

            if winner:
                scores[user2] = scores.get(user2, 0) + 1
            else:
                scores[user1] = scores.get(user1, 0) + 1
            outputMessage =""

            with open("scores.txt", "w") as file:
                for name in scores:
                    if name == user1 or name == user2:
                        outputMessage += f'{name}: {scores[name]}\n'
                        
                    file.write(f'{name}: {scores[name]}\n')
                await message.channel.send(f'```{outputMessage}```')
                    

            playing = False

        else:
            printmessage = name[0] + ' rolled a ' + str(currentRand) + '.'
            await message.channel.send(f'```{name[0]} rolled a {str(currentRand)}.```')
            gameover = False
            turnCount +=1
