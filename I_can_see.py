import os
import random

closet_interaction = False
sink_interaction = False
table_interaction = False
book_interaction = False
bread_interaction = False
coffee_interaction = False
bread_coffee_consumed = False
leave_house = False
game_running = False

import datetime

school_or_tution = ""

userday = datetime.datetime.now()
userday = userday.strftime("%A")
if userday == "Sunday" or userday == "Saturday":
	school_or_tution = "tuition"
else:
	school_or_tution = "school"

inventory = []

def interact_door():
	global leave_house

	os.system("cls")
	if leave_house == False and closet_interaction == True and sink_interaction == True and table_interaction == True and book_interaction == True and bread_interaction == True and coffee_interaction == True and bread_coffee_consumed == True:
		print("Knowing that you finished everything, you leave the house")
		leave_house = True
	else:
		print("You forgot something, maybe brushing your teeth? Collecting your books? Having breakfast? Changing into your attire?")


def interact_bed():
	os.system("cls")
	print("I'd really like to go back to bed, but I really have to leave the house.")

def interact_closet():
	global closet_interaction

	os.system("cls")
	if closet_interaction == False:
		print("(You open the closet door and take out a stack of clothes. You rub your finger against the studs on the shirt\nand find out that the shirt is red. You did the same for the jeans\nand it was the one you wanted to wear. You change into the clothes)")
		closet_interaction = True
	else:
		print("(You have already changed into your attire)")

def interact_table():
	global bread_coffee_consumed
	global school_or_tution
	global table_interaction

	os.system("cls")
	if table_interaction == False:
		if coffee_interaction == True and bread_interaction == True:
			print("(You sit down at the table. You listen to the latest pop playlists as you eat your breakfast.)")
			bread_coffee_consumed = True
			inventory.remove("Bread")
			inventory.remove("Coffee")
			table_interaction = True
		elif coffee_interaction == True:
			print("(You sit down at the table and realize that coffee won't be enough to fill your stomach.)")
		elif bread_interaction == True:
			print("(You sit down at the table and realize that you really like a warm dark coffee together with the bread for breakfast.)")
		else:
			print("(You sit down at the table and realize that you have to eat breakfast.)")
	else:
		print(f"(You decided not to sit down at the table again, you have to leave for {school_or_tution}.)")

def interact_sink():
	global sink_interaction
	global school_or_tution

	os.system("cls")
	if sink_interaction == False:
		print("(You brush your teeth and wash your face, you feel afresh)")
		sink_interaction = True
	else:
		if bread_coffee_consumed == True:
			print(f"(You have no time to waste. You have to get to {school_or_tution}.)")
		else:
			print("(You need to eat breakfast.)")


def pick_books():
	global book_interaction

	os.system("cls")
	if book_interaction == False:
		print("(You pick up the stack of books infront of you)")
		book_interaction = True
	else:
		print("(You have already packed your books.)")

def pick_coffee():
	global coffee_interaction

	os.system("cls")
	if coffee_interaction == False:
		print("(You pick up the cup of coffee you made the night before.)")
		coffee_interaction = True
	else:
		print("(You decided one cup of coffee was enough.)")

def pick_bread():
	global bread_interaction

	os.system("cls")
	if bread_interaction == False:
		print("(You pick up the piece of bread)")
		bread_interaction = True
	else:
		print("(You decided one piece of bread was enough.)")





grids = {
	"A1":{
		"s":"A2",
		"d":"B1"
	},
	"A2":{
		"w":"A1",
		"d":"B2",
		"s":"A3"

	},
	"A3":{
		"w":"A2",
		"d":"B3",
		"s":"A4"
	},
	"A4":{
		"w":"A3",
		"d":"B4"
	},
	"B1":{
		"s":"B2",
		"a":"A1",
		"item":{
			"name":"Bed",
			"pickable":False,
			"interactable":True,
			"consumable":False,
			"action":interact_bed
		}
	},
	"B2":{
		"w":"B1",
		"a":"A2",
		"item":{
			"name":"Books",
			"pickable":True,
			"interactable":False,
			"consumable":False,
			"action":pick_books
		}
	},
	"B3":{
		"d":"C3",
		"a":"A3"
	},
	"B4":{
		"d":"C4",
		"a":"A4",
		"item":{
			"name":"Closet",
			"pickable":False,
			"interactable":True,
			"consumable":False,
			"action":interact_closet
		}
	},
	"C1":{
		"s":"C2",
		"d":"D1",
		"item":{
			"name":"Door",
			"pickable":False,
			"interactable":True,
			"consumable":False,
			"action":interact_door
		}
	},
	"C2":{
		"w":"C1",
		"d":"D2",
		"s":"C3"
	},
	"C3":{
		"w":"C2",
		"d":"D3",
		"a":"B3"
	},
	"C4":{
		"d":"D4",
		"a":"B4"
	},
	"D1":{
		"s":"D2",
		"d":"E1",
		"a":"C1"
	},
	"D2":{
		"w":"D1",
		"d":"E2",
		"s":"D3",
		"a":"C2",
		"item":{
			"name":"Table",
			"pickable":False,
			"interactable":True,
			"consumable":False,
			"action":interact_table
		}
	},
	"D3":{
		"w":"D2",
		"d":"E3",
		"a":"C3"
	},
	"D4":{
		"a":"C4",
		"item":{
			"name":"Sink",
			"pickable":False,
			"interactable":True,
			"consumable":False,
			"action":interact_sink
		}
	},
	"E1":{
		"s":"E2",
		"d":"F1",
		"a":"D1"
	},
	"E2":{
		"w":"E1",
		"d":"F2",
		"s":"E3",
		"a":"D2"
	},
	"E3":{
		"w":"E2",
		"d":"F3",
		"s":"E4",
		"a":"D3"
	},
	"E4":{
		"w":"E3",
		"d":"F4",
	},
	"F1":{
		"s":"F2",
		"a":"E1",
		"item":{
			"name":"Coffee",
			"pickable":True,
			"interactable":False,
			"consumable":True,
			"action":pick_coffee
		}
	},
	"F2":{
		"w":"F1",
		"s":"F3",
		"a":"E2",
		"item":{
			"name":"Bread",
			"pickable":True,
			"interactable":False,
			"consumable":True,
			"action":pick_bread
		}
	},
	"F3":{
		"w":"F2",
		"s":"F4",
		"a":"E3"
	},
	"F4":{
		"w":"F3",
		"a":"E4"
	}
}

current_grid = "A1"


def mainmenu():
	global game_running
	os.system("cls")
	print("[I can see]")
	print("")
	print("<a> Begin game")
	print("<b> About game")
	print("<c> Leave")
	player_option = input(">> ").lower()
	os.system("cls")
	if player_option == "c":
		print("Goodbye <press enter>")
		input()
	elif player_option == "b":
		aboutmenu()
	elif player_option == "a":
		beginscene()
		game_running = True
	else:
		print("please input (a/b/c)")
		input()
		os.system("cls")
		mainmenu()

def aboutmenu():
	os.system("cls")
	print("This is a tiny game made by Pixo with the help of\nFirerousGT. It was something I decided to make because I got curious\nof how a day in life of a blind person is like. Pixo's website: pixoportfolio.carrd.co")
	print("<a> Main menu")
	player_option = input(">> ").lower()
	os.system("cls")
	if player_option == "a":
		mainmenu()
	else:
		print("please input (a)")
		input()
		os.system("cls")
		aboutmenu()

def beginscene():
	os.system("cls")
	print(f"(The morning symphony plays as you rise from your slumber.\n It's {userday} today. You have to attend {school_or_tution}.)")
	print("Press W,A,S,D to move, E to interact with objects and X to check you inventory")

def playerinteraction():
	global current_grid
	playerchoice = ""
	while playerchoice == "" and leave_house == False:
		playerchoice = input(">> ").lower()


	if (playerchoice == "w") or (playerchoice == "a") or (playerchoice == "s") or (playerchoice == "d"):
		if playerchoice in grids[current_grid]:
			current_grid = grids[current_grid][playerchoice]

			response = {
				"w": "forward",
				"a": "left",
				"s": "back",
				"d": "right"
			}.get(playerchoice)

			os.system("cls")
			print(f"You moved {response}")


		else:
			os.system("cls")
			there_is_a_wall = ["(You know your house well enough to know that there is a wall there.)", "(You plant your face into the wall)"]
			print(random.choice(there_is_a_wall))

	if playerchoice == "e":
		os.system("cls")
		if "item" in grids[current_grid]:
			if grids[current_grid]['item']['pickable'] == True:
				os.system("cls")
				grids[current_grid]["item"]["action"]()
				if not grids[current_grid]['item']['name'] in inventory:
					inventory.append(f"{grids[current_grid]['item']['name']}")
			elif grids[current_grid]["item"]["interactable"] == True:
				os.system("cls")
				grids[current_grid]["item"]["action"]()

	if playerchoice == "x":
		os.system("cls")
		print(f"{inventory}")


def gameend():
	global game_running
	game_running = False
	os.system("cls")
	print("(You grab the walking stick beside you door and leave the house) 'Here's to another day!'\nPress enter to continue.")
	input(">> ")
	os.system("cls")
	print("Thank you for playing [I Can See]!\nPress enter to exit!")
	input(">> ")



mainmenu()
while game_running:
	playerinteraction()
	if leave_house == True:
		gameend()
		break
