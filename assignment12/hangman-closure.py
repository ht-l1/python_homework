# Task 4 - Hangman Closure
# Declare a function called make_hangman() that has one argument called secret_word.
def make_hangman(secret_word):
    # It should also declare an empty array called guesses.
    guesses = []
    
    #  Within the function declare a function called hangman_closure() that takes one argument, which should be a letter. 
    def hangman_closure(letter):
        guesses.append(letter)
        
        # Within the inner function, each time it is called, the letter should be appended to the guesses array. Then the word should be printed out, with underscores substituted for the letters that haven't been guessed. So, if secret_word is "alphabet", and guesses is ["a", "h"], then "a__ha__" should be printed out. The function should return True if all the letters have been guessed, and False otherwise. 
        display_word = ""
        for char in secret_word:
            if char.lower() in [g.lower() for g in guesses]:
                display_word += char
            else:
                display_word += "_"
        
        print(display_word)
        
        return all(char.lower() in [g.lower() for g in guesses] for char in secret_word)
    
    # make_hangman() should return hangman_closure.
    return hangman_closure

# Within hangman-closure.py, implement a hangman game that uses make_hangman(). 
if __name__ == "__main__":
    secret = input("Enter the secret word: ")
    game = make_hangman(secret)
    
    print(f"Guess the word! It has {len(secret)} letters.")
    
    # Use the input() function to prompt for the secret word. Then use the input() function to prompt for each of the guesses, until the full word is guessed.
    while True:
        guess = input("Enter a letter: ")
        if len(guess) != 1:
            print("Please enter only one letter.")
            continue
            
        if game(guess):
            print("Congratulations! You guessed the word!")
            break