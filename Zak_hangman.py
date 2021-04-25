word="secret"

allowed_error=7
guesses=[]
done=False
while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter.upper(),end="  ")
        else:
            print("_",end="  ")
    print("")
    done=True

    guess=input(f"allowed error left {allowed_error} next :")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_error-=1
        if allowed_error==0:
            break
    done=True
    for letter in word:
        if letter.lower()  not in guesses:
            done=False


