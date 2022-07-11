def main():
    counter = 0
    greeting, counter = greet("Alice", counter)
    print(f"{greeting}\nCounter is {counter}")
    greeting, counter = greet("Bob", counter)
    print(f"{greeting}\nCounter is {counter}")

def greet(name, counter):
    return f"Hi, {name}!", counter + 1

main()
