__author__ = 'casey'

from Madlib import Madlib

class MadlibBuilder():

    def madlibParser(self):
        # Take whole_madlib and parse it by verb, noun, and adjective placeholders
        # For each "verb", "noun", and "adjective", parse and remove the word
        # add that word to user_prompt_list
        # Add each parsed section parsed_madlib
        pass

    def madlibInterpolator(self):
        # Iterate over whole_madlib and replace $VERB$ with first item in verb_list
        # Pop from list. Repeat for noun and adjective list

        while True:
            print("Interpolator initiated...")
            print("-->", madlib.whole_madlib)

            for word in madlib.whole_madlib.split():

                if "$VERB$" in word:
                    word.replace(madlib.verb_list(0))
                    print("verb replaced")
                    madlib.verb_list.pop(0)

            for word in madlib.whole_madlib.split():

                if "$NOUN$" in word:
                    word.replace(madlib.noun_list(0))
                    print("noun replaced")
                    madlib.noun_list.pop(0)

            for word in madlib.whole_madlib.split():

                if "$ADJECTIVE$" in word:
                    word.replace(madlib.adjective_list(0))
                    print("adjective replaced")
                    madlib.adjective_list.pop(0)

            #For testing
            print("Here's the new madlib: ")
            print(madlib.whole_madlib)
            break

madlib = Madlib("Road Trip")