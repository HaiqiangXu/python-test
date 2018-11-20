import sys

# Gather our code in a main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ... sys.argv[0] is the script name itself and can be ignored
    print('Hello there', sys.argv[0])
    print(repeat('why', 3, True))

    def x(a): return a + 10  # just add 10 to incoming value
    try:
        print(x(8))
    except NameError:
        print("Variable x is not defined")
    except:
        print("An unexpected exception occurred")

def repeat(text, times, exclaim):
    result = ""
    for x in range(times):
        result = result + text
    if exclaim:
        result = result + '!!!'

    return result

# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()
