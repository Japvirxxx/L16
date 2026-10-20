try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))

    result = num1 / num2 
    print(f"The result of {num1} divided by {num2} is: {result}")

except ZeroDivisionError as ex:
    print("Exception: ", ex)

except SyntaxError as ex:
    print("Exception: ", ex)

except:
    print("An unexpected error occurred.")

else:
    print("Division operation completed successfully.")

finally:
    print("This will execute no matter what.")