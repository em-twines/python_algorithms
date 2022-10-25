# Task 1: Declare a variable called favorite_number and store your favorite number with it. 
# Task 2: use the random module to generate a rand number etween a range that includes favorite_number
    #Determine how many numbers away the random number was from your fav number.

from operator import is_
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


#----------------------------------- pt 2------------------------------------------
#Task 1: Reverse a String
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



# Task 2: Capitalize a Letter
    # write code that takes a string as input and capitalizes the first letter of each word. Output as "Hello World".
    # steps: 
        # separate words into individual strings
        # use string.captialize()
        # print all strings together including their spaces

def capitalization(str_phrase):
    strs_phrase = str_phrase.split()
    output = ""
    for str in strs_phrase:
        output += str.capitalize()
        output += " "
    print(output)

capitalization("hello world")



# Task 3: Palindrome
    # Write code that takes user input and checks to see if it's a palindrome as well as reports the results. 
    # steps
        # define palindrome condition
            # identify ver_string forwards
            # identify ver_string backwards
            # if forwards == backwards, then palendrome
        # get input
        # if input == palindrome
        # print true phrase
        # else print false phrase

def palindrome(word):
    is_palindrome = False
    forward = word
    backward = ""
    for index in range(len(word) -1, -1, -1):
        backward += word[index]
    if forward == backward:
        is_palindrome == True 
        print(f"{word.capitalize()} is a palendrome!")
    else:
        print(f"{word.capitalize()} is not a palendrome.")

palindrome("racecar")


# Bonus Challenge
# Task 4: compress repeated letters to a number then the letter they are the number of
    # steps
        # identify repeated letters
        # compress to the number form of how many there are
        # print 
    
def check_consecutive(string): 
    output = []
    count = 1
    output1 = []
    index = 1

    for char in string:
        while len(string) >= (index + 1):
            char = string[index-1 ]
            curr = string[index]
            if char == curr:
                count += 1 
                index += 1
                if index == len(string): 
                    output1 += char   
                    index += 1
                    output.append(count)
                    count = 1
                    output1 += curr
            else:
                output1 += char   
                index += 1
                output.append(count)
                count = 1

    merged_output = merge_list(output, output1)
    print(merged_output)

def merge_list(list1, list2):
    list_final = []
    length_1 = len(list1)
    length_2 = len(list2)
    if length_1 >= length_2:
        length = length_2
        item = 0
        while item < length:
            list_final += str(list1[item]), list2[item]
            item += 1
        list_final_joined = "".join(list_final)
        list_final_joined + (list2[item])

    else: 
        length = length_1
        item = 0
        while item < length:
            list_final += str(list1[item]), list2[item]
            item += 1
        list_final_joined = "".join(list_final)
        list_final_joined + (list2[item])
    return list_final_joined


check_consecutive("aaabbbbbccccaacccbbbaaabbbaaa")



#----------------------------------- pt 3------------------------------------------
