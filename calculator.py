# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

if __name__ == "__main__":
    print("==== Simple Calculator ====")

    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid number, please try again.")
            continue

        if choice == '1':
            print("✅ Result:", add(a, b))
        elif choice == '2':
            print("✅ Result:", subtract(a, b))
        elif choice == '3':
            print("✅ Result:", multiply(a, b))
        elif choice == '4':
            print("✅ Result:", divide(a, b))
        else:
            print("❌ Invalid choice, please select from 1-5.")

