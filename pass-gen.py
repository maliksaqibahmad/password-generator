import random

def generate_random_password(length):
      """Generates a random password of the specified length."""
      characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-={}[]|;':\",./<>?"
      
      if length > len(characters):
          raise ValueError("Password length exceeds the number of unique characters available.")
      password = ''.join(random.sample(characters, length))
      return password

if __name__ == "__main__":
      
      while True:
          try:
              userNumber = int(input("Enter a number between 1 and 10: "))
              if 1 <= userNumber <= 10:
                  break
              else:
                  print("Please enter a number within the range!")
          except ValueError:
              print("Invalid input! Please enter a valid number.")
      
      try:
          password = generate_random_password(userNumber)
          print("Generated password:", password)
      except ValueError as e:
          print(e)
