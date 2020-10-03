# This program is a short chat bot recommending musical artists to the user based upon genre input.

from random import choice

def get_bot_response(user_response):

  # lofi beats to chill/study to
  bot_response_lofi = ["Birocratic", "Dusty Decks", "Kino B",  "Giants Nest","Blue Steel", "gate"]
  # hip hop
  bot_response_hiphop = ["Nas", "Common", "Kendrick Lamar", "Kid Cudi"]
  # all the cringe rock of the 00s
  bot_response_rock = ["Creed", "Nickelback", "Three Days Grace", "3 Doors Down"]
  # electronic
  bot_response_electronic = ["Jai Gourgaud", "Astron" "Zircon", "Ronald Jenkees", "The Field"]
  # country
  bot_response_country = ["Haha, just kidding. I don't listen to country, sorry!", "Tricked you! Country is gross, hard pass on that one."]
  # classical
  bot_response_classical = ["Beethoven", "Mozart", "Debussy", "Tchaikovsky", "Eric Whitaker"]
  # if the user doesn't want recommendations, but just wants to talk about music
  bot_response_listening = ["\nFeel free to vent away, friend."]

  if user_response == "lofi":
    return choice(bot_response_lofi)
  elif user_response == "hip hop":
    return choice(bot_response_hiphop)
  elif user_response == "rock":
    return choice(bot_response_rock)
  elif user_response == "electronic":
    return choice(bot_response_electronic)
  elif user_response == "country":
    return choice(bot_response_country)
  elif user_response == "classical":
    return choice(bot_response_classical)
  elif user_response == "talk":
    print(choice(bot_response_listening))
    user_vent = input("Go ahead and say whatever it is you want. \n \n")
    return "\nGlad you got that off your chest."
  else:
    return "\nHmm, sorry, I'm not sure what you mean by that."

# function to get a single usable word for the genre, just in case the user enters a sentence with the genre
def getValidGenre():

  prompt = "\nI'll try my best to put you on something new. I'm into lofi, hip hop, rock, electronic, country, and classical. \n"
  print(prompt)

  # genre list for validation check
  genreList = ["lofi", "hip hop", "rock", "electronic",  "country", "classical"]
  userGenre = input("What genre do you want recommendations for? ")

  # prompt for genre until the user gets it
  while userGenre not in genreList:
    userGenre = input("\nI'm not sure what you mean, can you try again with just the genre, please: \n")
  # return valid genre
  return userGenre


def main():
  print("Hey I'm music bot! I'd love to (ideally) talk about music with you.")

  user_response = ""

  while "bye" not in user_response:
    user_response = input("\nDo you want some music recommendations or do you just want to talk? If you're done chatting, just say bye before you go! \n \n")

    # exit if the user said bye in any way
    if "bye" in user_response:
      break
    # recommendations prompt for genre
    elif "recommendations" in user_response:
      user_response = getValidGenre()
      print("\nI think you would like: ")
    # set user_response to "talk" if that was in their response, as users may not solely enter "talk"
    elif "talk" in user_response:
      user_response = "talk"

    # call get_bot_response for the response and print
    bot_response = get_bot_response(user_response)
    print(bot_response)

main()