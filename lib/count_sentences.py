class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        else:
            self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = [sentence for sentence in self.value.split('.') if sentence]
        sentences += [sentence for sentence in self.value.split('!') if sentence]
        sentences += [sentence for sentence in self.value.split('?') if sentence]
        return len(sentences)
