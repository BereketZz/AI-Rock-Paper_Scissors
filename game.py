import tkinter as tk
from PIL import Image, ImageTk
import random


OPTIONS = ["rock", "paper", "scissors"]


score = {"player": 0, "computer": 0}

# function to generate random option
def get_computer_choice():
    return random.choice(OPTIONS)

# Create a function to handle player clicks
def player_choice(player_option):
    # Get the computer's choice
    computer_option = get_computer_choice()

    # Determine the winner
    if player_option == computer_option:
        result = "Tie"
    elif (player_option == "rock" and computer_option == "scissors" or
          player_option == "paper" and computer_option == "rock" or
          player_option == "scissors" and computer_option == "paper"):
        result = "You win!"
        score["player"] += 1
    else:
        result = "Computer wins!"
        score["computer"] += 1
    
    # Update the score 
    score_label.config(text="Player: {}  Computer: {}".format(score["player"], score["computer"]))
    
    # Update the result 
    result_label.config(text=result, font=("Arial", 16, "bold"), justify="center")
    
   
    player_image = ImageTk.PhotoImage(Image.open(player_option + ".jpg").resize((100, 100)))
    computer_image = ImageTk.PhotoImage(Image.open(computer_option + ".jpg").resize((100, 100)))

    image_label1 = tk.Label(root, image=player_image)
    image_label2 = tk.Label(root, image=computer_image)


  
   
    
   # Update the player and computer choice displays
    player_choice_label.config(image=player_image)
    player_choice_label.image = player_image
    computer_choice_label.config(image=computer_image)
    computer_choice_label.image = computer_image

# Create the GUI
root = tk.Tk()
root.configure(background="teal")
root.title("Rock_Paper_Scissors")
root.geometry("600x500")

# Create the buttons for the game options
rock_image = ImageTk.PhotoImage(Image.open("rock.jpg").resize((100, 100)))
rock_button = tk.Button(root, image=rock_image, command=lambda: player_choice("rock"))
rock_button.pack(side=tk.LEFT, padx=10, pady=10)

paper_image = ImageTk.PhotoImage(Image.open("paper.jpg").resize((100, 100)))
paper_button = tk.Button(root, image=paper_image, command=lambda: player_choice("paper"))
paper_button.pack(side=tk.LEFT, padx=10, pady=10)

scissors_image = ImageTk.PhotoImage(Image.open("scissors.jpg").resize((100, 100)))
scissors_button = tk.Button(root, image=scissors_image, command=lambda: player_choice("scissors"))
scissors_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create the label to display the result of each game
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Create the label to display the player's choice
pp_label = tk.Label(root, text="player")
pp_label.config(font=("Arial", 12,"bold"))
player_choice_label = tk.Label(root, image=None)
player_choice_label.pack(side=tk.LEFT, padx=10)
player_choice_label.place(x=50, y=50)
pp_label.place(x=250, y=20, anchor="ne")


# Create the label to display the computer's choice
cp_label = tk.Label(root, text="computer")
cp_label.config(font=("Arial", 12,"bold"))
computer_choice_label = tk.Label(root, image=None)
computer_choice_label.pack(side=tk.LEFT, padx=10)
computer_choice_label.place(x=200, y=50)

cp_label.place(x=120, y=20, anchor="ne")

# Create the label to display the score
score_label = tk.Label(root, text="Player: 0  Computer: 0")
score_label.pack()

# Start the main loop
root.mainloop()




