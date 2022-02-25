import csv

print("Welcome to the Email List Cleaner")
print()

# specify filenames in the current directory
infile_name = "prospects.csv"
outfile_name = "prospects_clean.csv"

# display filenames
print("Source list:  ", infile_name)
print("Cleaned list: ", outfile_name)
print()

with open(infile_name, "r", newline='') as infile, \
     open(outfile_name, "w", newline='') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # read each row of the data
    for row in reader:
        # create a new row to store the clean data
        new_row = []

        # clean the data
        new_row.append(row[0].strip().title())
        new_row.append(row[1].strip().title())
        new_row.append(row[2].strip().lower())

        # write the clean data to a file
        writer.writerow(new_row)
        
print("Congratulations! Your list has been cleaned!")
