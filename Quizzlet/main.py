import random
def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    correct_count=0
    count=0
    
    while count<8:
        for i in translations:
            answer=str(input(f"What is the Spanish translation for {i}? "))
            if translations[i]==answer:
                correct_count+=1
                print("That is correct!\n")
            else:
                print(f"That is incorrect, the Spanish translation for {i} is {translations[i]}.\n")   
            count+=1
        #print(count)

    print(f"You got {correct_count}/{count} words correct, come study again soon!")

if __name__ == '__main__':
    main()