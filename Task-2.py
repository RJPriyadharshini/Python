#3 . using a python lambda function to create a fibonacci serious from 1 to 50 elements?
# Function to generate Fibonacci series using lambda function
fibonacci = lambda n: [0, 1] if n == 2 else (fibonacci(n - 1) + [fibonacci(n - 1)[-1] + fibonacci(n - 1)[-2]])

# Generate Fibonacci series from 1 to 50 elements using lambda function
fib_series = fibonacci(50)

# Print the generated Fibonacci series
print("Fibonacci Series (1 to 50 elements):", fib_series)