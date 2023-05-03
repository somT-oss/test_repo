from main import read_file, write_file


def test_write_file():
    file = "new.txt"
    assert write_file("New Content", file) == "Successfully wrote to the file " + file

def test_read_file():
    # Test case 1: Read a file that exists
    expected_output = "New Content"
    file_path = "new.txt"
    with open(file_path, "w") as f:
        f.write(expected_output)
    assert read_file(file_path) == expected_output