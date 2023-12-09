import io
import sys
import pytest
from count_sentences import MyString

class TestMyString:
    '''MyString in count_sentences.py'''

    def test_is_class(self):
        '''is a class with the name "MyString".'''
        string = MyString()
        assert type(string) == MyString

    def test_value_string(self):
        '''raises a ValueError with the message "The value must be a string." if not string.'''
        with pytest.raises(ValueError, match="The value must be a string.") as exc_info:
            string = MyString(value=123)

    def test_is_sentence(self):
        '''returns True if value ends with a period and False otherwise.'''
        assert MyString("Hello World.").is_sentence() == True
        assert MyString("Hello World").is_sentence() == False

    def test_is_question(self):
        '''returns True if value ends with a question mark and False otherwise.'''
        assert MyString("Is anybody there?").is_question() == True
        assert MyString("Is anybody there").is_question() == False

    def test_is_exclamation(self):
        '''returns True if value ends with an exclamation mark and False otherwise.'''
        assert MyString("It's me!").is_exclamation() == True
        assert MyString("It's me").is_exclamation() == False

    def test_count_sentences(self):
        '''returns the number of sentences in the value.'''
        simple_string = MyString("one. two. three?")
        empty_string = MyString()
        complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
        assert simple_string.count_sentences() == 3
        assert empty_string.count_sentences() == 0
        assert complex_string.count_sentences() == 4