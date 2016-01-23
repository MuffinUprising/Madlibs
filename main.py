from Madlib import Madlib
from MadlibBuilder import MadlibBuilder

__author__ = 'casey'

class main():


    # Prompt User
    def promptUser(self):
        print("Thank you for choosing the Madlib Generator 6000!")
        username = input("What is your name?")
        print("Nice to meet you, ", username)

        UI.displayMenu()


    # User Menu
    def displayMenu(self):

        global madlib
        while True:
            for madlibStr in madlib_list:
                print(madlibStr)
            break

        madlib_choice = int(input("Please choose a Madlib:"))

        # UI.chooseMadlib()

        #  Road Trip
        if madlib_choice == 1:
           UI.buildRoadTrip(madlib)
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
    def requestVerb(self):
        temp_verb = input("Please enter a verb: ")
        madlib.verb_list.append(temp_verb)


    # Request Noun
    def requestNoun(self):
        temp_noun = input("Please enter a noun: ")
        madlib.noun_list.append(temp_noun)


    # Request Adjective
    def requestAdjective(self):
        temp_adj = input("Please enter an adjective: ")
        madlib.adjective_list.append(temp_adj)



    # Word Choice
    def wordChoice(self):
        # Iterate through user_prompt_list.
        # Display word choice to user and get response
        while True:
            for word in user_prompt_list:
                if word == "$VERB$":
                    UI.requestVerb()

                elif word == "$NOUN$":
                    UI.requestNoun()

                elif word == "$ADJECTIVE$":
                    UI.requestAdjective()

            # For testing
            print("verb list:")
            for verb in madlib.verb_list:
                print(verb)
            print("\n")

            print("noun list:")
            for noun in madlib.noun_list:
                print(noun)
            print("\n")

            print("adjective list:")
            for adj in madlib.adjective_list:
                print(adj)
            print("\n")

            UI.madlibInterpolator()


    # Display new Madlib
    def displayNewMadlib(self):
        # Print the final Madlib to the user
        pass

    # Add Road Trip data to madlib
    def buildRoadTrip(self, madlib):


        road_trip = "Last summer my family and I went on a road trip to Yellowstone Park. \n" \
                   "We $ADJECTIVE$ in the family $NOUN$ at dawn and headed west. To our surprise, \n" \
                   "the our pet $NOUN$ , Frosty was $VERB$ ing behind the back seat. We had no \n" \
                   "choice but to $VERB$ him with us. The only problem is that we didn't \n" \
                   "bring his $NOUN$ . He $ADJECTIVE$ s it, but it is the only to get him to $VERB$ \n" \
                   "for that long. We made it to Yellowstone anyway and Frosty was a good \n" \
                   "$NOUN$ for the entire trip. Yellowstone was $ADJECTIVE$ , I guess."

        madlib.whole_madlib = road_trip

        #for testing
        print(madlib.whole_madlib)

        #build user prompt list
        UI.buildUserPromptList()


    def buildUserPromptList(self):

        for word in madlib.whole_madlib.split():
            if "$VERB$" in word or "$ADJECTIVE$" in word or "$NOUN$" in word:
                user_prompt_list.append(word)

        # for testing
        for prompt in user_prompt_list:
            print(prompt)

    def madlibInterpolator(self):
        # Iterate over whole_madlib and replace $VERB$ with first item in verb_list
        # Pop from list. Repeat for noun and adjective list
        new_madlib = madlib.whole_madlib

        while True:
            print("Interpolator initiated...")
            print("-->", new_madlib)

            for word in new_madlib.split():

                if "$VERB$" in word:
                    temp_verb = madlib.verb_list.pop(0)
                    print(temp_verb)
                    word.replace('$VERB$', temp_verb)
                    print("verb replaced")

                if "$NOUN$" in word:
                    temp_noun = madlib.noun_list.pop(0)
                    print(temp_noun)
                    word.replace('$NOUN$', temp_noun)
                    print("noun replaced")

                if "$ADJECTIVE$" in word:
                    temp_adj = madlib.adjective_list.pop(0)
                    print(temp_adj)
                    word.replace('$ADJECTIVE$', temp_adj)
                    print("adjective replaced")


            # for word in new_madlib.split():
            #
            #     # if "$NOUN$" in word:
            #     temp_noun = madlib.noun_list.pop(0)
            #     print(temp_noun)
            #     word.replace('$NOUN$', temp_noun)
            #     print("noun replaced")
            #
            #
            # for word in new_madlib.split():
            #
            #     # if "$ADJECTIVE$" in word:
            #     temp_adj = madlib.adjective_list.pop(0)
            #     print(temp_adj)
            #     word.replace('$ADJECTIVE$', temp_adj, madlib.adjective_list.length)
            #     print("adjective replaced")


            #For testing
            print("Here's the new madlib: ")
            print(new_madlib)
            break



UI = main()

madlib = Madlib("")

# builder = MadlibBuilder()

madlib_list = ("(1)Road Trip", "(2)A Trip to the Dentist", "(3)Moons of Jupiter")

user_madlib = int

user_prompt_list = []

UI.promptUser()