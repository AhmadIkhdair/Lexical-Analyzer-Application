class Lexer:
    def __init__(self):
        pass

    # Lex Method
    @staticmethod
    def get_token(user_input, index, similar_ids, symbol_table):
        reserved_words = ["for", "while", "if", "else"]
        result = None
        # Check if the user input is a numeric value
        if user_input.isnumeric():
            result = f'<token=INTEGER, integer_value={user_input}>'

        # Check if the user input is a reserved word
        elif user_input in reserved_words:
            result =  f'<token={user_input.upper()}>'

        # Check if the user input is a floating-point number
        elif '.' in user_input:
            try:
                float_value = float(user_input)
                result =  f'<token=FLOAT, float_value={user_input}>'
            except ValueError:
                pass

        # Check if the user input is a negative integer
        elif '-' in user_input and user_input[1:].isdigit():
            result =  f'<token=INTEGER, integer_value={user_input}>'

        # Check for logical operators
        elif user_input == "&&":
            result =  '<token=LOGICAL_AND>'
        elif user_input == "||":
            result = '<token=LOGICAL_OR>'
        elif user_input == "|":
            result = '<token=BITWISE_OR>'

        # Check if the user input is an identifier
        elif user_input[0].isalpha() or user_input[0] == '_':
            if user_input in similar_ids: # Identifier already stored
                print(f'<token=ID, index={similar_ids.index(user_input) + 4}>') 
            else: # New Identifier
                similar_ids.append(user_input)
                index += 1
                print(f'<token=ID, index={index}>')
                # Append to symbol table
                symbol_table[index] = user_input

        # Handle unrecognized tokens / strings
        else:
            result = f'<token=ERROR, unrecognized_string="{user_input}">'

        if result:
            print(result)

        # Return updated index, similar_ids list, and symbol_table
        return index, similar_ids, symbol_table


# Show Table Method
def show_table(symbol_table):
    reserved_words = ["for", "while", "if", "else"]
    index = len(reserved_words)

    # Print the symbol table
    print("--------------------")
    for i, word in enumerate(reserved_words, start=0): # Printing reserved words
        print(f'index={i}, symbol="{word}"')
    for idx, symbol in symbol_table.items(): # Printing new stored identifiers
        print(f'index={idx}, symbol="{symbol}"')
    print("--------------------")


# Main method
def main():
    print("Welcome To the Lexical Analyzer")
    similar_ids = []
    symbol_table = {}  # Initialize symbol table
    index = 3  # Starting index
    count = 0
    while True:
        print("\nMENU")
        print("1- Call Lex")
        print("2- Show Symbol Table")
        print("3- Exit")
        user_input = input("Please choose a command: ")
        if user_input == "1": # Call lex
            data = []
            with open("lab2.txt", "r") as input_file:
                lines = input_file.read().split("\n")
                word_lists = [[word.strip() for word in line.split(' ')] for line in lines]
                for word_list in word_lists:
                    data += word_list

            if count < len(data):
                # Update symbol_table using the get_token method
                token = Lexer.get_token(data[count], index, similar_ids, symbol_table)
                if isinstance(token, tuple):
                    index, similar_ids, symbol_table = token 
                count += 1
            else:
                print("reached the end")

        elif user_input == "2": # Show table
            print("\nShowing Symbol Table")
            show_table(symbol_table)
        elif user_input == "3": # Exit program
            print("Exiting")
            break
        else:
            print("Not a valid command")


if __name__ == "__main__":
    main()
