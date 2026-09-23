filename = "sample.txt"

with open(filename, "w") as file:
    file.write("This is a sample file created for the internship task.\n")
    file.write("Python file manipulation is simple and useful.")

with open(filename, "r") as file:
    content = file.read()

print("File created successfully.")
print("File contents:")
print(content)

with open(filename, "a") as file:
    file.write("\nAdditional content added successfully.")

print("Content appended successfully.")