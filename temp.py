import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    try:
        c = float(sys.argv[1])
    except IndexError:
        c = float(input("Enter temperature in Celsius: "))
    except ValueError:
        print("Please enter a valid number.")
        sys.exit(1)

    print("Fahrenheit:", celsius_to_fahrenheit(c))

