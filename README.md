# Solving_Wordle_Using_Information_Theory
What is Wordle?
  Worlde is a simpe game, every day a new secret word is chosen as the daily puzzle’s solution. Players must follow the rules in order to find out which word it is.
  The daily solution is randomly chosen from a list of commonly used five-letter words. Our task is to find this secret word in six or less tries. 
  In each attempt, the player is allowed to input a five-letter word and receives clues pointing towards the answer in the form of colors over each input letter. 
  The goal of the game is not only to find the secret word but also to achieve it using as few attempts as possible.
      1. Every letter that is not present in the solution will have its background turn gray.
      2. The background of letters that are present in the solution but are misplaced will become yellow.
      3. Letters that are both present in the solution and placed in the correct position will get a green background.

Here I am using Information Theory concept to solve the Wordle game.If you want to know about information theory please look into this file https://towardsdatascience.com/information-theory-applied-to-wordle-b63b34a6538e 

compute_entropies_allwords.py:
  I generate the entropies for all 5 letter words using allowed_words.txt ,stored in entropies_for_allwords_sorted.txt in desecending order.
Wordle.py:
  Here iam writing all functions that are used to solve wordle. Maintain the every condtion to reduce number of 5 letter words.
Wordle_GUI.py:
  This for graphical user interface to play wordle. Iam using Tkinter here to make simple GUI and add fucntionalites with respective to users input.
  GUI is divided into 4 parts.
    1.Title
    2.Entering the Words
    3.Showing the recommended words to reduce the number of steps to reach final word.
    4.Final result
