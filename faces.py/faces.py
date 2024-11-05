def main():
    # Get User Input
    msg = input("Enter your message: ")
    # Call convert function
    result = convert(msg)
    # Print the result
    print(result)

def convert(msg):
    # Replace :) for happy emoji
    msg1 = msg.replace(":)", '🙂')
    # Replace :( for sad emoji
    msg2 = msg1.replace(":(", '🙁')
    # Return string
    return msg2

main()
