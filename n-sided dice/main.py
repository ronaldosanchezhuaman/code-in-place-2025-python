import random

def main():
    dado=int(input("How many sides does your dice have?"))
    number_ramdom= random.randint(1,dado)

    print(f"Your roll is {number_ramdom}")

if __name__ == '__main__':
    main()