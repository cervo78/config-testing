import pytest
import difflib

before_file = "config/config_file_before_change.txt"
after_file = "config/config_file_after_change.txt"

@pytest.fixture
def read_files():
    with open(before_file, 'r') as f_before, open(after_file, 'r') as f_after:
        before_content = f_before.readlines()
        after_content = f_after.readlines()
    return before_content, after_content

def test_configuration_change(read_files):
    before_content, after_content = read_files

    # Compare the files line by line using difflib
    diff = list(difflib.unified_diff(before_content, after_content, lineterm="", fromfile="before", tofile="after"))
    
    # Check that there are differences
    assert diff, "Configuration files have no differences."
    
    # Example assertion: Check that the new parameter is in the "after" file
    assert any("parameter3" in line for line in diff), "Expected change not found in configuration."

    # Optionally, print the diff for debugging
    print("\n".join(diff))
