def main():
    # Prompt the user for a temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert the temperature to Celsius using the formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Output the result
    print("Temperature: " + str(fahrenheit) + "F = " + str(celsius) + "C")

if __name__ == '__main__':
    main()
