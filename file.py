import sys

sys.argv = ['file.py', 'text.txt']
if len(sys.argv) != 2:
    print("Error: Please provide the name of the file.")
    sys.exit(1)
filename = sys.argv[1]
try:
    infile = open(filename, 'r')
    line_number = 1
    for line in infile:
        line = line.strip()
        values = line.split()
        if len(values) != 2:
            print("Error in line " + str(line_number) + ": ")
        else:
            try:
                num1 = float(values[0])
                num2 = float(values[1])
                print("Sum of line " + str(line_number) + ": " + str(num1 + num2))
            except ValueError:
                print("Error in line " + str(line_number) + ":")
        line_number += 1
    infile.close()
except FileNotFoundError:
    print("Error: File '" + filename + "' not found.")