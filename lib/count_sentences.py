import re

class MyString:
    def __init__(self, value=""):
        # Initialize with an empty string if no value is provided
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        
        self.value = value

    def is_sentence(self):
        # Check if the value ends with a period
        return self.value.endswith('.')

    def is_question(self):
        # Check if the value ends with a question mark
        return self.value.endswith('?')

    def is_exclamation(self):
        # Check if the value ends with an exclamation mark
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the value into sentences based on '.', '?', and '!'
        sentences = [sentence.strip() for sentence in re.split(r'[.!?]', self.value) if sentence]
        return len(sentences)


