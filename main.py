"""main module"""
import game

kitchen = game.Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = game.Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = game.Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

bathroom = game.Room("Bathroom")
ballroom.set_description("Dark room with cobwebs at the corners.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(bathroom, 'south')
bathroom.link_room(ballroom, 'north')

dave = game.Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

tabitha = game.Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)

friend = game.Friend("Timon", "He looks friendly.")
friend.set_conversation("I can help you. Whose weakness do you want to know about?.")
bathroom.set_character(friend)

cheese = game.Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = game.Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

coffee = game.Item("coffee")
coffee.set_description("Hot! Be careful not to get burned!")
bathroom.set_item(coffee)

current_room = kitchen
backpack = []

dead = False

while not dead:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        previous_room, current_room = current_room, current_room.move(command)
        if not current_room:
            print('No such room.')
            current_room = previous_room
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
            if inhabitant.status == 'friend' and not inhabitant.help:
                name_enemy = input('> ')
                weakness = inhabitant.set_power(name_enemy)
                if not weakness:
                    print('You have no such enemies.')
                else:
                    print(weakness)

    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input('> ')

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with):
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None

                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
