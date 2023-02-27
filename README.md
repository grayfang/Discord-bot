# Discord-bot
A silly little bot that allows users to "death roll" and do other games.
After adding the discord api token on line 77 and running the bot you can call the command $help to get a list of the commands and what they do

On start up the program will 

open the list of scores
open the list of foods
$d20
  will generate a random number from 1-20 and print a little blurb if the user rolls a 1 or 20
$start 
  will start a death roll game in which the users will get a random number from 1-1000 
  then on the next message from another user the user will get a random number from 1-the previous number and so on
  and the player who gets a 1 loses and the winner's score gets incremented
  the scores and the username of the players will be stored in a file scores.txt 
$stop
  will stop the code by using sys.exit(0) to allow the user to shut down the bot if needed, working on checking if the game is still going before closing
