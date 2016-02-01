__author__ = 'casey'

import unittest

from main import madlib
from main import main


class UnitTests(unittest.TestCase):


    def test_build_user_prompt_list(self):
        # Test variables
        test_whole_madlib = "A B C $VERB$ D E $NOUN$ F G H I $ADJECTIVE$ J K L $NOUN$ M N" \
                                "O P Q $VERB$ R S T $ADJECTIVE$ "

        temp_user_prompt_list = ["$VERB$", "$NOUN$", "$ADJECTIVE$", "$NOUN$", "$VERB$", "$ADJECTIVE$"]
        temp_user_choice = 1


        # Edit variables in instance of Madlib
        madlib.whole_madlib = test_whole_madlib

        self.assertEquals(main().buildUserPromptList, temp_user_prompt_list, "it worked!")


    # def test_add_new_words(self):
        test_verb_list = ["run", "jump"]
        test_noun_list = ["house", "car"]
        test_adjective_list = ["delightful", "crummy"]

        madlib.verb_list = test_verb_list
        madlib.noun_list = test_noun_list
        madlib.adjective_list = test_adjective_list
        madlib.madlib_choice = temp_user_choice

        test_output = "A B C run D E house F G H I delightful J K L car M N" \
                                "O P Q jump R S T crummy "

        self.assertEquals(main.addNewWords(main), test_output, "it worked!")



