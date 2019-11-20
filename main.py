def fibonacci_seq(num1, num2, count=1):
    if count == 100:
        return
    print(num1 + num2)
    return fibonacci_seq(num2, num1+num2,count+1)
if __name__ == "__main__":
    fibonacci_seq(0,1)