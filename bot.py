import discord
import sys
import foods
import dice
import scores
from game_logic import is_over, play_game

MAX_RANGE = 1000
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

playing = False


@client.event
async def on_ready():
    
    print(f'We have logged in as {client.user}')
    # Load the list of foods from the file
    foods.load_foods()
    scores.load_scores()

@client.event
async def on_message(message):
    global MAX_RANGE
    global playing


    if message.author == client.user:
        return



    # Handle the "foods" and "food" commands
    if message.content.lower().startswith('$foods') or message.content.lower().startswith('$food'):
        await message.channel.send(f'Pierre should eat {foods.get_random_food()}.')

    elif message.content.lower().startswith('$addfood'):
        await message.channel.send(f'```Please enter the name of the food you would like to add to the list or type $cancel to cancel adding a food to the list```')
        message = await client.wait_for('message')
        if message.content.lower().startswith('$cancel'):
            return
        while message.author == client.user:
            message = await client.wait_for('message')
        food = message.content
        foods.add_food(food)
        await message.channel.send(f'```Added {food} to the list```')
        food.load_foods()

    elif message.content.lower().startswith('$reload'):
        foods.load_foods()
        await message.channel.send("```Food list has been reloaded```")

    elif message.content.lower().startswith('$d20'):
      await message.channel.send(f'```{str(message.author).split("#")[0]} {dice.roll_d20()}```')

    elif message.content.lower().startswith('$scores'):
        await message.channel.send(scores.print_scores())
            

#edit to make sure game aint going
    if message.content.lower() =='$stop' and is_over() == True:
        await message.channel.send(f'```Shutting down.```')
        sys.exit(0)
    elif message.content.lower() =='$stop':
        await message.channel.send(f'```There is currently a game going on, please wait.```')
    if message.content.lower().startswith('$start'):
        scores_dict = scores.get_scores()
        print(scores_dict)
        await play_game(message, client, scores_dict)


    if message.content.lower().startswith('$help'):
      await message.channel.send(f'```Commands:\n$foods or $food: Return a random food for Pierre to eat.\n$addfood: Add a new food to the list.\n$reload: Reload the list of foods.\n$scores: Get the current scores.\n$d20: Roll a d20.\n$start: Start the random number game.```')


#token here          
client.run('')