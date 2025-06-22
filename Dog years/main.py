# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    Dog_year= float(input("Enter an age in calendar years:"))
    Human_years=Dog_year*DOG_YEARS_MULTIPLIER

    print(f"That's {Human_years} in dog years!")



# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()