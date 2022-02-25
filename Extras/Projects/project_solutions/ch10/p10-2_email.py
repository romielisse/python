import csv

def main():
    print("Email Creator")
    print()

    # specify filenames in the current directory
    list_filename = "email.csv"
    template_filename = "email_template.txt"

    template = ""
    with open(template_filename, "r") as file:
        template = file.read()

    with open(list_filename, "r", newline='') as file:
        reader = csv.reader(file)

        # read each row of the data
        for row in reader:
            # clean the data
            first_name = row[0].strip().title()
            email = row[2].strip().lower()

            email_text = template.replace("{first_name}", first_name)
            email_text = email_text.replace("{email}", email)

            print("=" * 64)
            print(email_text)


if __name__ == "__main__":
    main()
