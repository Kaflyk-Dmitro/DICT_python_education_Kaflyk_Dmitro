def display_help():
    help_text = """
    Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
    Special commands: !help !done
    """
    print(help_text)

def main():
    formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
    result = []
    
    while True:
        user_input = input("Choose a formatter: ")
        
        if user_input == "!help":
            display_help()
        elif user_input == "!done":
            save_to_file(result)
            print("Exiting program...")
            break
        elif user_input in formatters:
            handle_formatter(user_input, result)
        else:
            print("Unknown formatting type or command. Please try again.")

def handle_formatter(formatter, result):
    if formatter == "plain":
        text = input("Text: ")
        result.append(text)
    elif formatter == "bold":
        text = input("Text: ")
        result.append(f"**{text}**")
    elif formatter == "italic":
        text = input("Text: ")
        result.append(f"*{text}*")
    elif formatter == "header":
        level = int(input("Level: "))
        text = input("Text: ")
        result.append(f"{'#' * level} {text}")
    elif formatter == "link":
        label = input("Label: ")
        url = input("URL: ")
        result.append(f"[{label}]({url})")
    elif formatter == "inline-code":
        text = input("Text: ")
        result.append(f"`{text}`")
    elif formatter == "ordered-list" or formatter == "unordered-list":
        handle_list(formatter, result)
    elif formatter == "new-line":
        result.append("\n")

def handle_list(formatter, result):
    items = []
    count = int(input("Number of items: "))
    if count <= 0:
        print("The number of items should be greater than zero.")
        return
    for i in range(count):
        item = input(f"Item {i + 1}: ")
        if formatter == "ordered-list":
            items.append(f"{i + 1}. {item}")
        else:
            items.append(f"* {item}")
    result.extend(items)

def save_to_file(result):
    with open("output.md", "w") as file:
        file.write("\n".join(result))

if __name__ == "__main__":
    main()
