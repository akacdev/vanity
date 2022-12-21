from tempfile import NamedTemporaryFile
from shutil import move

input_file = "input.txt"
output_file = "output.txt"

seen_lines = set()

with NamedTemporaryFile('w', delete=False) as output, open(input_file) as input:
    for line in open(input_file, "r"):
        sline = line.rstrip('\n')
        if sline not in seen_lines:
            output.write(line)
            seen_lines.add(sline)
move(output.name, output_file)