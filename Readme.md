# Student Progression Predictor

## Overview
This program predicts progression outcomes for multiple students based on their pass, defer, and fail credits.

## Project Context
This is my first-year project for the programming principles module. The goal is to create a simple program that assists in predicting student progression outcomes.

## Getting Started
1. Run the program by executing the Python script.
2. Follow the prompts to input pass, defer, and fail credits for each student.
3. The program will provide progression predictions for each student.

## Code Explanation
- The program uses a while loop to repeatedly prompt the user for input until they decide to end the program by entering 'q'.
- Input validation is implemented to ensure that the entered credits are within the specified range.
- The `progres_report` function calculates and prints the progression outcome based on the input credits.
- The final count of different progression outcomes is displayed at the end.

## Usage
- Input pass, defer, and fail credits within the specified range (0 to 120, in increments of 20).
- The program will calculate the total credits and predict the progression outcome.
- The final count of different progression outcomes will be displayed.
