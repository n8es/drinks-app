from drink_converter import DrinkConverter
from drinking_game import DrinkingGame

def main():
    print("Welcome to the Drinks App!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Use the Smart Drink Converter")
        print("2. Play the Interactive Drinking Game")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            converter = DrinkConverter()
            print("\n--- Smart Drink Converter ---")
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the unit to convert from (ml, l, oz, cup, pint, quart, gallon): ").lower()
            to_unit = input("Enter the unit to convert to (ml, l, oz, cup, pint, quart, gallon): ").lower()

            result = converter.convert(value, from_unit, to_unit)

            if result is not None:
                print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
            else:
                print("Invalid units provided.")

        elif choice == '2':
            game = DrinkingGame()
            print("\n--- Interactive Drinking Game ---")
            input("Press Enter to spin the wheel...")
            challenge = game.spin()
            print(f"\nThe wheel landed on: {challenge}")

        elif choice == '3':
            print("Thanks for using the Drinks App!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()