from Madlib import Madlib

__author__ = 'casey'

class main():


    # Prompt User
    def promptUser(self):
        print("Thank you for choosing the Madlib Generator 6000!")
        username = input("What is your name?")
        print("Nice to meet you, %s", username)

        UI.displayMenu()


    # User Menu
    def displayMenu(self):

        while True:
            for madlib in madlib_list:
                print(madlib)
            break

        madlib_choice = int(input("Please choose a Madlib:"))
        # UI.user_madlib = madlib_choice

        # UI.chooseMadlib()

        #  Road Trip
        if madlib_choice == 1:
           UI.buildRoadTrip()
           UI.wordChoice()

        # Trip to the Dentist
        elif madlib_choice == 2:
            print("Sorry, no trip to the dentist is available at this time")
            UI.displayMenu()
        # Moons of Jupiter
        elif madlib_choice == 3:
            print("sorry, there are no moon of Jupiter to explore at this time")
            UI.displayMenu()
        else:
            print("Please enter choices 1-3")
            UI.displayMenu()


    # Choose Madlib
    def chooseMadlib(self):
        #  Road Trip
        if user_madlib == "1":
            madlib.name = "Road Trip"
            UI.buildRoadTrip(madlib)
            UI.wordChoice()

        # Trip to the Dentist
        elif user_madlib == "2":
            print("Sorry, no trip to the dentist is available at this time")
            UI.displayMenu()
        # Moons of Jupiter
        elif user_madlib == "3":
            print("sorry, there are no moons of Jupiter to explore at this time")
            UI.displayMenu()
        else:
            print("Please enter choices 1-3")
            UI.displayMenu()


    # Request Verb
    def requestVerb(self, madlib):
        temp_verb = input("Please enter a verb: ")
        madlib.verb_list.add(temp_verb)


    # Request Noun
    def requestNoun(self, madlib):
        temp_noun = input("Please enter a noun: ")
        madlib.verb_list.add(temp_noun)


    # Request Adjective
    def requestAdjective(self, madlib):
        temp_adj = input("Please enter an adjective: ")
        madlib.adjective_list.add(temp_adj)



    # Word Choice
    def wordChoice(self, user_prompt_list):
        # Iterate through user_prompt_list.
        # Display word choice to user and get response
        for word in user_prompt_list:
            if word == "verb":
                UI.requestVerb()

            elif word == "noun":
                UI.requestNoun()

            elif word == "adjective":
                UI.requestAdjective()


    # Display new Madlib
    def displayNewMadlib(self):
        # Print the final Madlib to the user
        pass

    # Add Road Trip data to madlib
    def buildRoadTrip(self, madlib):


        road_trip = "Last summer my family and I went on a road trip to Yellowstone Park. \n" \
                   "We adjective in the family noun at dawn and headed west. To our surprise, \n" \
                   "the our pet noun, Frosty was verbing behind the back seat. We had no \n" \
                   "choice but to verb him with us. The only problem is that we didn't \n" \
                   "bring his noun. He adjectives it, but it is the only to get him to verb \n" \
                   "for that long. We made it to Yellowstone anyway and Frosty was a good \n" \
                   "noun for the entire trip. Yellowstone was adjective, I guess."

        madlib.whole_madlib = road_trip


UI = main()

madlib = Madlib("")

madlib_list = ("(1)Road Trip", "(2)A Trip to the Dentist", "(3)Moons of Jupiter")

user_madlib = int

user_prompt_list = ()

UI.promptUser()