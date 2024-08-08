import streamlit as st

# Define arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Streamlit UI
def main():
    st.title("Simple Calculator")

    # Input fields for numbers
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Radio buttons for operation selection
    operation = st.radio("Choose an operation:", ('Add', 'Subtract', 'Multiply', 'Divide'))

    # Calculate and display the result
    if st.button("Calculate"):
        if operation == 'Add':
            result = add(num1, num2)
        elif operation == 'Subtract':
            result = subtract(num1, num2)
        elif operation == 'Multiply':
            result = multiply(num1, num2)
        elif operation == 'Divide':
            result = divide(num1, num2)
        
        st.write(f"The result is: {result}")

if __name__ == "__main__":
    main()
