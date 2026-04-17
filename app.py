def calculate_factorial(n):
    if n < 0:
        return "Error: Negative number"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    num = 7
    final_val = calculate_factorial(num)
    
    # Save to results.txt in the root of the container
    with open("results.txt", "w") as f:
        f.write(f"Factorial of {num} is {final_val}")
    
    print(f"Logic completed. Result: {final_val}")
    print("This is a factorial code")