import random

def main():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    answer = (num1 + num2)

    print("Khansole Academy")
    print(f"What is {num1} + {num2}?")
    useranswer = int(input("Your answer: "))
    
    if (answer==useranswer):
        print("Correct!")
    else:
        print(f"Incorrect.")
        print(f"The expected answer is {num1 + num2}.")


    
if __name__ == '__main__':
    main()