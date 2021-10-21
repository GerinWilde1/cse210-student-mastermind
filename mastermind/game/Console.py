import random


class Console:


    def read(self, prompt):

        return input(prompt)

    def write(self, text):

        print(text)
    
    def read_number(self, prompt):

        return int(input(prompt))