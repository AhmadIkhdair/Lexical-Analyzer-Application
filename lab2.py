class Lexer:
    def __init__(self):
        pass

    #Get Lex Method
    @staticmethod
    def get_token(user_input, index, similar_ids):
        reserved_words = ["for", "while", "if", "else"]
        
        # Check if the user input is a numeric value
        if user_input.isnumeric():
            return f'<token=INTEGER, integer_value={user_input}>'
        
        # Check if the user input is a reserved word
        elif user_input in reserved_words:
            return f'<token={user_input.upper()}>'
        
        # Check if the user input is a floating-point number
        elif '.' in user_input:
            try:
                float_value = float(user_input)
                return f'<token=FLOAT, float_value={user_input}>'
            except ValueError:
                pass
        
        # Check if the user input is a negative integer
        elif '-' in user_input and user_input[1:].isdigit():
            return f'<token=INTEGER, integer_value={user_input}>'
        
        # Check for logical operators
        elif user_input == "&&":
            return '<token=LOGICAL_AND>'
        elif user_input == "||":
            return '<token=LOGICAL_OR>'
        elif user_input == "|":
            return '<token=BITWISE_OR>'
        
        # Check if the user input is an identifier
        elif user_input[0].isalpha() or user_input[0] == '_':
            if user_input in similar_ids:
                print(f'<token=ID, index={similar_ids.index(user_input) + 4}>')
            else:
                similar_ids.append(user_input)
                index += 1
                print(f'<token=ID, index={index}>')
        
        # Return similar_ids list for unrecognized tokens
        return index, similar_ids

# Show Table Method
def show_table():
    reserved_words = ["for", "while", "if", "else"]
    similar_id = []
    index = len(reserved_words) + 1
    with open("lab2.txt", "r") as file:
        data = file.read().split()
        for i in data:
            if i.isnumeric():
                print(f'<token=INTEGER, integer_value={i}>')
            elif i in reserved_words:
                print(f'<token={i.upper()}>')
            elif '-' in i and '.' in i:
                print(f'<token=FLOAT, float_value={i}>')
            elif '.' in i:
                print(f'<token=FLOAT, float_value={i}>')
            elif '-' in i:
                print(f'<token=INTEGER, integer_value={i}>')
            elif "&&" == i:
                print(f'<token=LOGICAL_AND>')
            elif "||" == i:
                print(f'<token=LOGICAL_OR>')
            elif "|" == i:
                print(f'<token=BITWISE_OR>')
            elif i[0].isdigit():
                print(f'<token=ERROR, unrecognized_string="{i}">')
            else:
                if i not in similar_id:
                    similar_id.append(i)
                print(f'<token=ID, index={similar_id.index(i) + index}>')

    # Print the symbol table
    print("Symbol Table:")
    for i, identifier in enumerate(similar_id, start=index):
        print(f'<token=ID, index={i}>')



def main():
    print("Welcome To the Lexical Analyzer")
    similar_ids = []
    index = 5  # Starting index
    while True:
        print("\nMENU")
        print("1- Call Lex")
        print("2- Show Symbol Table")
        print("3- Exit")
        user_input = input("Please choose a command: ")

        if user_input == "1":
            count = 0
            with open("lab2.txt", "r") as file:
                data = file.read().split()
            while count < len(data):
                token = Lexer.get_token(data[count], index, similar_ids)
                if isinstance(token, tuple):
                    index, similar_ids = token  # Update index and similar_ids
                count += 1
        elif user_input == "2":
            print("Showing table")
            show_table()
        elif user_input == "3":
            print("Exiting")
            break
        else:
            print("Not a valid command")

if __name__ == "__main__":
    main()
