# Simple Calculator Program

This is a basic calculator program implemented in Python. It allows the user to perform four fundamental arithmetic operations: addition, subtraction, multiplication, and division. The program continues to run until the user chooses to exit.

## Features

- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division of two numbers
- User-friendly menu for selecting operations
- Continuous operation until the user decides to exit

## Requirements

To run this program, you need to have Python installed on your system.

## Installation

1. **Install Python:**

   Make sure you have Python installed. You can download and install Python from the official website: [Python.org](https://www.python.org/downloads/)

   To check if Python is already installed, you can run the following command in your terminal or command prompt:

   ```sh
   python --version
   ```

   or

   ```sh
   python3 --version
   ```

2. **Download the Code:**

   Clone or download this repository to your local machine.

   ```sh
   git clone https://github.com/yourusername/calculator.git
   ```

   Navigate to the directory where you have saved the code.

   ```sh
   cd calculator
   ```

## How to Run the Program

1. Open your terminal or command prompt.
2. Navigate to the directory where the code is saved.
3. Run the following command to start the program:

   ```sh
   python calculator.py
   ```

   or

   ```sh
   python3 calculator.py
   ```

## Usage

1. When the program starts, you will see a menu with options to perform addition, subtraction, multiplication, division, or exit the program.
2. Select the desired operation by entering the corresponding letter (A, B, C, D, or E).
3. Follow the prompts to enter the two numbers for the chosen operation.
4. The result of the operation will be displayed.
5. The menu will be shown again, and you can continue performing operations until you choose to exit by selecting 'E'.

## Example

```
A. Addition
B. Subtraction
C. Multiplication
D. Division
E. Exit

give your choice: A
addition of the two numbers. Give those two numbers now:-
Enter the first number: 5
Enter the second number: 3
5 + 3 = 8

A. Addition
B. Subtraction
C. Multiplication
D. Division
E. Exit

give your choice: E
program Ended!
```

## Notes

- The division operation will raise a `ZeroDivisionError` if the second number is zero. Ensure that the second number is non-zero for division.
- The program handles integer inputs. For floating-point operations, you can modify the input prompts to accept `float` values instead of `int`.

## Contributing

If you find any bugs or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License.
