import random
n = random.randint(1, 100) 
a = -1
guesses = 1
while(a != n):
    try:
        userInput = input("Guess the number: ")
        a = int(userInput)
    except ValueError:
        print("Please enter a valid number.")
        continue 
    if(a >n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number Please")
        guesses +=1

print(f"You have guessed the number {n} correctly in {guesses} attempts")