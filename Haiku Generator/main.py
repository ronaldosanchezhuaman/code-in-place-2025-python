from ai import call_gpt

def main():
    # TODO: your code here
    name= input("Enter your name: ")
    topic= input("Enter a topic:")
    #
    print("Creating your haiku...")
    haiku=call_gpt(f"to turn the name {name} and topic into a haiku {topic}")
    print(haiku)


if __name__ == "__main__":
    main()