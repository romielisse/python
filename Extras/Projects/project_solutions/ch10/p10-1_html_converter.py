def main():
    print("HTML Converter")
    print()

    # specify filename in the current directory
    filename = "groceries.html"

    html = ""
    with open(filename, "r") as file:
        for line in file:
            html += line.lstrip()

    text = html \
        .replace("<h1>", "") \
        .replace("</h1>", "") \
        .replace("<ul>", "") \
        .replace("</ul>", "") \
        .replace("<li>", "* ") \
        .replace("</li>", "") \
        .replace("\n\n", "\n") \
        .strip() 
    
    print(text)


if __name__ == "__main__":
    main()
