import random

def generate_word():
      random_word = ''
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      number_of_letters = random.randint(3, 10)
      for i in range(0, number_of_letters, 1):
          random_letter = random.choice(alphabet)
          random_word += random_letter
      return random_word
