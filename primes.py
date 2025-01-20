from flask import Flask
import random
from sympy import primerange

app = Flask(__name__)

@app.route("/")
def hello_world():


    # Generate a list of 6-digit primes
    six_digit_primes = list(sympy.primerange(100000, 1000000)) 

    # Generate a list of 8-digit primes
    eight_digit_primes = list(sympy.primerange(10000000, 100000000))  # All 8-digit primes

    # Generate a list of 10-digit primes
    ten_digit_primes = list(sympy.primerange(1000000000, 10000000000))

    print(f"6-digit primes: {six_digit_primes}")
    print(f"8-digit primes: {eight_digit_primes}")
    print(f"10-digit primes: {ten_digit_primes}")
    
    # Randomly select primes from each list
    random_six_digit_prime = random.choice(six_digit_primes)
    random_eight_digit_prime = random.choice(eight_digit_primes)
    random_ten_digit_prime = random.choice(ten_digit_primes)

    print(f"Random 6-digit prime: {random_six_digit_prime}")
    print(f"Random 8-digit prime: {random_eight_digit_prime}")
    print(f"Random 10-digit prime: {random_ten_digit_prime}")
    
if __name__ == "__main__":
    app.run(debug=True)