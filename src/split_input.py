from pathlib import Path
from sys import path
input_file = Path(__file__).parents[1] /"data"/"input.txt"
lines = input_file.read_text(encoding="UTF-8").splitlines(keepends=True)
Number_of_lines = 50
total_line = len(lines)
base_lines = len(lines) // Number_of_lines
extra_lines = len(lines) % Number_of_lines
start = 0
for i in range(1 , Number_of_lines+1):
    lines_of_this_file = base_lines
    if i <= extra_lines:
        lines_of_this_file +=1
    end = start + lines_of_this_file
    file_lines = lines[start:end]
    output_file = input_file.parent / f"input_{i}.txt"
    output_file.write_text("".join(file_lines),encoding="UTF-8")
    start = end
print(f"Split {total_line} lines into {Number_of_lines} files with {base_lines} lines each and {extra_lines} extra lines distributed among the first {extra_lines} files.")
