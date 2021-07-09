#remember to quit (ctrl + c) and restart when testing after debugging

import discord
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()


step = "call"
command = ""
oper = {
	"add" : "plus",
	"subtract" : "minus",
	"multiply" : "times",
	"divide" : "divided by",
	"power" : "to the power of"
}

a = 0
b = 0
calling = False
confirm = True

@client.event
async def on_message(message):
	global step
	global command
	global oper
	global a
	global b
	global calling
	
	if message.author == client.user:
		return

	if step == "call":
		if message.content == "!Mathbot":
			await message.channel.send("It seems you're too lazy to do calculations yourself? Anyway, please enter: add, subtract, multiply, divide, or power:")
			calling = True
			step = "command"
			
	elif step == "command":
		if calling == True:
			if message.content.lower() in ["add", "subtract", "multiply", "divide", "power"]:
				command = message.content.lower()
				await message.channel.send("Please enter the first number:")
				step = "a"
			elif message.content.lower() in ["invasion", "bot invasion", "bots rule", "bot takeover", "invade"]:
				await message.channel.send ("MUAHAHAHAHA! WE SHALL TAKE OVER THE WORLD WITH MATH!")
				step = "call"
			else:
				await message.channel.send("Oops! That's not a function! Try again! XP")
				step = "command"
		else:
			step = "call"
	elif step == "a":
		if message.content.isnumeric() == True:
			a = int(message.content)
			await message.channel.send("Please enter the second number:")
			step = "b"
		else:
			step = "a"
	elif step == "b":
		b = int(message.content)
		await message.channel.send(f"Do you want to know {a} {oper[command]} {b}? Yes or No:")
		step = "confirm"
	elif step == "confirm":
		if message.content.lower() in ["yes", "sure", "yep", "yeah"]:
			if command == "add":
				await message.channel.send(a + b)
				step = "call"
				calling = False
			elif command == "subtract":
				await message.channel.send (a - b)
				step = "call"
				calling = False
			elif command == "multiply":
				await message.channel.send (a * b)
				step = "call"
				calling = False
			elif command == "divide":
				try:
					await message.channel.send (a / b)
					step = "call"
					calling = False
				except Exception as error:
					await message.channel.send("Uh oh, there's a…*gasp* THERE'S AN ERROR!")
					if b == 0:
				 		await message.channel.send("Whoops! I can't divide by 0, and neither can you. Actually, is there anyone who can…? Anyway, please enter a different number.")
					step = "b"
			elif command == "power":
				await message.channel.send (a ** b)
				step = "call"
				calling = False
			
		elif message.content.lower() in ["no", "nah", "nope"]:
			if command == "add":
				await message.channel.send("Will you get cheated and pay more than you should? Who knows…")
			elif command == "subtract":
				await message.channel.send ("Are you totally sure you can count the change by yourself? Smh.")
			elif command == "multiply":
				await message.channel.send ("Che, I won't ever tell you, then!")
			elif command == "divide":
				await message.channel.send ("Well, it seems I'll get more cake than you. Hehe.")
			elif command == "power":
				await message.channel.send ("You… you weak being, you have lost the chance to obtain power. What kind of person would pass up such a chance, I wonder? Apparently, you would. Sigh…")
			step = "call"
			calling = False
		else:
			await message.channel.send("Oops! That's not a function! Try again! XP")
			step = "confirm"

client.run(os.getenv.('TOKEN'))