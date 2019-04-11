#Import functions
import time
import pickle
import random

menu=0
class1_results=[]
class2_results=[]
class3_results=[]
retry=("You have already taken this test, let's retry.")
error=("There was an error in your input, please retry.")
operators=('+','-','*')

def main():
    number1=0
    number2=0
    counter=0
    correct_answer=0
    correct_answers=0
    wrong_answers=0
    group_correct=0
    name=input("Please enter your name: ")
    while group_correct!=1:
        group_selection1=input("Please enter which class you are in (1, 2 or 3): ")
        if group_selection1 == '1' or group_selection1 == '2' or group_selection1 == '3':
            group_correct=1
        else:
            print(error)
    while counter!=10:
        #Declare variables from while
        number1=random.randint(1,10)
        number2=random.randint(1,10)
        operator=operators[random.randint(0,2)]
        answer=int(input("{0}{1}{2}= ".format(number1,operator,number2)))
        if operator=='+':
            correct_answer=number1+number2   
        elif operator=='-':
            correct_answer=number1-number2
        elif operator=='*':
            correct_answer=number1*number2
        if answer==correct_answer:
            print("Correct")
            correct_answers=correct_answers+1
        else:
            print("Incorrect")
            wrong_answers=wrong_answers+1
        counter=counter+1
    print("You got {0} questions correct.".format(correct_answers))
    print("You got {0} questions wrong.".format(wrong_answers))
    print("You're total score is {0}/10.".format(correct_answers))
    if group_selection1=='1':
        if name in class2_results:
            print('') #Add the results to the existing entry in the list. (still needs to be added)
        else:
            new_student=[name,correct_answers]
            class2_results.append(new_student)
    elif group_selection1=='2':
        if name in class2_results:
            print('') #Add the results to the existing entry in the list. (still needs to be added)
        else:
            new_student=[name,correct_answers]
            class2_results.append(new_student)
    elif group_selection1=='3':
        if name in class3_results:
            print('') #Add the results to the existing entry in the list. (still needs to be added)
        else:
            new_student=[name,correct_answers]
            class3_results.append(new_student)

def print_results():
    group_correct=0
    while group_correct!=1:
        group_selection2=input("Please enter which class you are in (1, 2 or 3): ")
        if group_selection2 =='1':
            group_correct=1
            print(class1_results)
                    
        elif group_selection2 =='2':
            group_correct=1
            print(class2_results)
            
        elif group_selection2 =='3':
            group_correct=1
            print(class3_results)
            
        else:
            print(error)

while menu!=1:
    menu_correct=0
    while menu_correct!=1:
        print("****Menu****")
        print("1) Run the test.")
        print("2) Print the test results")
        choice=int(input("Please make a choice (1 or 2): "))
        if choice==1:
            menu_correct=1
            main()
        elif choice==2:
            menu_correct=1
            print_results()
        else:
            print(error)
