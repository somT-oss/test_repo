def write_file(content: str, file: str) -> str: 
    with open(file, "w") as f:
        f.write(content)
        return "Successfully wrote to the file " + file


def read_file(file_name: str) -> str:
    with open(file_name) as f:
        for line in f:
            return line

write = write_file("New Content", "new.txt")
print(write)