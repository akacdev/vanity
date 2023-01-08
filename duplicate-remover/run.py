from tempfile import NamedTemporaryFile
from shutil import move

input_file = "input.txt" # add your words each on a new lone into this file input.txt --- make sure there is no spaces in front or at the end of your words ---
output_file = "output.txt" # this file will have all the doubles removed

seen_lines = set()

with NamedTemporaryFile('w', delete=False) as output, open(input_file) as input:
    for line in open(input_file, "r"):
        sline = line.rstrip('\n')
        if sline not in seen_lines:
            output.write(line)
            seen_lines.add(sline)
move(output.name, output_file)