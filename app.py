from flask import Flask
import time
import sympy


app = Flask(__name__)

@app.route("/")
def hello_world():
    # Question 2
    print("Hello, we made to batch 2")
   # Question 2



    # List of prime numbers (pairwise)
    prime_numbers = [10000019, 10000169]

    # Function to compute the private key 'd'
    def private_key(p, q, e):
        # Euler's totient function: phi(n) = (p-1)*(q-1)
        phi_n = (p - 1) * (q - 1)

        start_time = time.time()  # Start timing the brute-force process

        d = None

        # Brute-forcing to find d such that (d * e) % phi_n == 1
        for i in range(1, phi_n):
            if (i * e) % phi_n == 1:
                d = i  # Found the private key 'd'
                break

        end_time = time.time()  # End timing the brute-force process

        total_time_taken = end_time - start_time  # Calculate the total time taken

        return d, total_time_taken


    e = 13  # Public exponent
    times = []  # List to store the times for each pair of primes
    digits = []  # List to store the number of digits for each prime pair

    # Loop through each pair of prime numbers
    for i in range(0, len(prime_numbers), 2):
        p = prime_numbers[i]
        q = prime_numbers[i + 1]

        # Calculates the private key 'd' and time taken
        d, total_time = private_key(p, q, e)

        # Stores the results
        times.append(total_time)
        digits.append(len(str(p)))  # Get the number of digits in the prime number 'p'

        print(f"\nFor {len(str(p))}-digit primes:")
        print(f"p = {p}, q = {q}")
        print(f"d = {d} in {total_time:.5f} seconds")
            
    
if __name__ == "__main__":
    app.run(debug=False)