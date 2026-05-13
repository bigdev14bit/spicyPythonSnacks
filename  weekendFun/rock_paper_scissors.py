while True:
    #first_person = input("PLAYER ONE: Enter (ROCK, PAPER, OR SCISSORS): ").lower()

    first_person = input("\nPLAYER ONE: Enter (ROCK, PAPER, OR SCISSORS): ")

    if first_person == "quit":
        print("  \nTERMINATED!!  ")
        break

    second_person = input("PLAYER TWO: Enter (ROCK, PAPER, OR SCISSORS): ")

    #second_person = input("PLAYER TWO: Enter (ROCK, PAPER, OR SCISSORS): ").lower()
#idk why .lower() not working here

    if first_person == second_person:
        print(" \nIT'S A TIE ")
    else:

      if first_person == "Rock":
          if second_person == "Scissors":
            print(" \nPlayer One Wins ")
          else:
            print(" \nPlayer Two Wins ")

      elif first_person == "Paper":
          if second_person == "Rock":
              print(" \nPlayer One Wins ")
          else:
              print(" \nPlayer Two Wins ")

      elif first_person == "Scissors":
          if second_person == "Paper":
            print(" \nPlayer One Wins ")
          else:
              print(" \nPlayer Two Wins ")
