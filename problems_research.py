# Task 1: Declare a variable called favorite_number and store your favorite number with it. 
# Task 2: use the random module to generate a rand number etween a range that includes favorite_number
    #Determine how many numbers away the random number was from your fav number.

import random

favorite_number = 24

def gen_rand_num():
    result = random.randint(0, 100)
    return result

def abs_diff(num1, num2):
    diff_btw = (num1 - num2)
    answer = abs(diff_btw)
    return answer

rand_num = gen_rand_num()
answer = abs_diff(rand_num, favorite_number)
print(rand_num, favorite_number)
print(answer)




# Task 3: create a while loop that generates a rand num and checks if it matches fav num
    # Keep track of how many times the computer has guessed.
    #display a message explaining how many attempts it took to get it right.

favorite_number = 24


rand_num = gen_rand_num()
counter = 0
while rand_num != favorite_number:
    rand_num = gen_rand_num()
    counter += 1
print(f"It took the computer {counter} guesses to arrive at my favorite number, {favorite_number}.")



#Task 4: Reverse a String
    # steps: 
        # store string value
        # get last letter
        # print last letter
        # get subsequent last letters
        # add these to the printed variable

def reverse_string(string):
    output = ""
    index = len(string)-1
    while len(output)< len(string):
        output += string[index]
        index -=1
    print (output)

reverse_string("hello")

#or

def reverse_string1(string):
    reversed_word = ''
    for index in range(len(string) -1, -1, -1):
        reversed_word += string[index]
    print(reversed_word)

reverse_string1("hello")




