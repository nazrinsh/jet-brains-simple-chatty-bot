from smtpd import program


def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print("Please, remind me your name.")
    name = input()
    print(f"What a great name you have {name}.")


def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

    print(f"Your age is {your_age}; that's a good time to start programming!")


def count():
    print("Now I will prove to you that I can count to any number you want.")
    number = int(input())
    b = 0
    while b <= number:
        print(b, "!")
        b = b + 1
    print("Completed have a nice day!")


def test():
    print("Let's test your programming knowledge.")
    # write your code here\
    print("Why do we use methods?\n1. To repeat a statement multiple times.\n2. To decompose a program into several small subroutines.\n3. To determine the execution time of a program.\n4. To interrupt the execution of a program.")
    while True:
        choose = int(input())
        if choose != 2:
            print("Please, try again.")
        else:
            print("Completed, have a nice day!")
            break


def end():
    print('Congratulations, have a nice day!')


greet('A', '2022')  
remind_name()
guess_age()
count()
test()
end()
