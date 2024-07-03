from fibonacci import fibo

def main():
    try:
        n = int(input("Enter the fibonacci number length: "))
        if n < 0:
            print("Please enter positive integer.")
        else:
            sequence = fibo(n)
            print(f"The length of {n} from the fibonacci: ")
            print(sequence)
    except ValueError:
        print("only number allowed")

if __name__ == "__main__":
    main()