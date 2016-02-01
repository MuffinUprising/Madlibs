from Madlib import Madlib
from MadlibBuilder import MadlibBuilder

__author__ = 'casey'

def main():


    # Prompt User
    def promptUser():
        print("Thank you for choosing the Madlib Generator 6000!")
        # username = input("What is your name?")
        # print("Nice to meet you,", username)

        displayMenu()

    # User Menu
    def displayMenu():

        global madlib
        while True:
            for madlib_str in madlib_list:
                print(madlib_str)
            break

        madlib_choice = int(input("Please choose a Madlib:"))

        #  Road Trip
        if madlib_choice == 1:
           buildRoadTrip(madlib)
           wordChoice()

        # Trip to the Dentist
        elif madlib_choice == 2:
            print("Sorry, no trip to the dentist is available at this time, bummer. \n")
            displayMenu()
        # Moons of Jupiter
        elif madlib_choice == 3:
            print("sorry, there are no moons of Jupiter to explore at this time.\n")
            displayMenu()
        else:
            print("Please enter choices 1-3. \n")
            displayMenu()

    # Request Verb
    def requestVerb():
        temp_verb = input("Please enter a verb: ")
        madlib.verb_list.append(temp_verb)

    # Request Noun
    def requestNoun():
        temp_noun = input("Please enter a noun: ")
        madlib.noun_list.append(temp_noun)

    # Request Adjective
    def requestAdjective():
        temp_adj = input("Please enter an adjective: ")
        madlib.adjective_list.append(temp_adj)

    # Word Choice
    def wordChoice():
        # Iterate through user_prompt_list.
        # Display word choice to user and get response
        while True:
            for word in user_prompt_list:
                if word == "$VERB$":
                    requestVerb()

                elif word == "$NOUN$":
                    requestNoun()

                elif word == "$ADJECTIVE$":
                    requestAdjective()

            addNewWords()

    # Display new Madlib
    def displayNewMadlib():
        # Print the final Madlib to the user
        pass

    # Add Road Trip data to madlib
    def buildRoadTrip(madlib):

        road_trip = "Last summer my family and I went on a road trip to Yellowstone Park. \n" \
                   "We $VERB$ in the family $NOUN$ at dawn and headed west. To our surprise, \n" \
                   "the our pet $NOUN$ , Frosty was $VERB$ ing behind the back seat. We had no \n" \
                   "choice but to $VERB$ him with us. The only problem is that we didn't \n" \
                   "bring his $NOUN$ . He $VERB$ s it, but it is the only to get him to $VERB$ \n" \
                   "for that long. We made it to Yellowstone anyway and Frosty was a good \n" \
                   "$NOUN$ for the entire trip. Yellowstone was $ADJECTIVE$ , I guess."

        madlib.whole_madlib = road_trip

        #build user prompt list
        buildUserPromptList()

    # Build list of prompts based on madlib
    def buildUserPromptList():

        for word in madlib.whole_madlib.split():
            if "$VERB$" in word or "$ADJECTIVE$" in word or "$NOUN$" in word:
                user_prompt_list.append(word)

    # Add word to madlib and pass to Madlib object
    def addNewWords():

        # Counters
        verb_count = 0
        noun_count = 0
        adj_count = 0

        # Temp Lists
        temp_verb_list = madlib.verb_list
        temp_noun_list = madlib.noun_list
        temp_adj_list = madlib.adjective_list

        # Temp Madlib
        temp_madlib = madlib.whole_madlib

        # Iterate through madlib and replace verb placeholders with new verbs
        while verb_count < len(temp_verb_list):
            print("Adding verbs...")
            for word in temp_madlib.split(" "):
                if "$VERB$" in word:
                    temp_verb = temp_verb_list.pop(0)
                    print(temp_verb)
                    temp_madlib = temp_madlib.replace(word, temp_verb, 1)
                    print("verb replaced")
                    verb_count += 1

        # Iterate through madlib and replace noun placeholders with new nouns
        while noun_count < len(temp_noun_list):
            print("Adding nouns...")
            for word in temp_madlib.split(" "):
                if "$NOUN$" in word:
                    temp_noun = temp_noun_list.pop(0)
                    print(temp_noun)
                    temp_madlib = temp_madlib.replace(word, temp_noun, 1)
                    print("noun replaced")
                    noun_count += 1

        # Iterate through madlib and replace adjective placeholders with new adjectives
        while adj_count < len(temp_adj_list):
            print("Adding adjectives...")
            for word in temp_madlib.split(" "):
                if "$ADJECTIVE$" in word:
                    temp_adj = temp_adj_list.pop(0)
                    print(temp_adj)
                    temp_madlib = temp_madlib.replace(word, temp_adj, 1)
                    print("adjective replaced")
                    adj_count += 1

            # Display result to user and set madlib.new_madlib
            print("Here's the new madlib: ")
            madlib.new_madlib = temp_madlib
            print(madlib.new_madlib)
            playAgain()

    # Prompt the user to play again
    def playAgain():

        another = input("Would you like to play again? Y/N")

        if another is "Y":
            displayMenu()
        elif another is "N":
            print("Thanks for playing!")
            displayMenu()
        else:
            print("Please choose Y or N")
            playAgain()





if '__name__' == '__main__':
    main()
# else:
#     UI = main()

madlib = Madlib("")

builder = MadlibBuilder()

madlib_list = ("(1)Road Trip", "(2)A Trip to the Dentist", "(3)Moons of Jupiter")

user_madlib = int

user_prompt_list = []

# main.promptUser()

