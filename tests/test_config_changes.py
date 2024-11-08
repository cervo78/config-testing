import pytest

# Sample test to compare two configuration files
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def test_config_changes():
    # Read before and after config files
    before_config = read_file("config/config_file_before_change.txt")
    after_config = read_file("config/config_file_after_change.txt")

    # Assert expected changes (for example, IP address and route)
    assert "ip address 192.168.2.1" in after_config  # Check for changed IP before and afeter
    assert "ip route 0.0.0.0 0.0.0.0 192.168.1.254" in after_config  # Check for new route
    assert "ip address 192.168.1.1" not in after_config  # Ensure old IP is not present
