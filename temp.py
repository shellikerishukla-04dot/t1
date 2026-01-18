import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":

    if len(sys.argv) > 1:
        celsius = float(sys.argv[1])   # Jenkins parameter
    else:
        celsius = 25.0                 # Default value

    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Celsius:", celsius)
    print("Fahrenheit:", fahrenheit)