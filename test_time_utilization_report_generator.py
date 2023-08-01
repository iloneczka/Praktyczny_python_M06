import os
import pytest
import re
from typing import Dict

from time_utilization_report_generator import load_entries_from_csv, count_time_by_tag, display_tag_and_time, Entry

# Test data
CSV_CONTENT = """desc,time,tags
Task 1,60,projectA clientX
Task 2,30,projectB clientX
Task 3,45,projectA
Task 4,15,projectB"""

# Helper function to create a temporary CSV file
def create_temp_csv_file(content):
    with open('temp.csv', 'w') as f:
        f.write(content)
    return 'temp.csv'

def test_load_entries_from_csv():
    csv_file = create_temp_csv_file(CSV_CONTENT)
    entries = load_entries_from_csv(csv_file)

    assert len(entries) == 4
    assert isinstance(entries[0], Entry)
    assert entries[0].desc == "Task 1"
    assert entries[0].time == 60
    assert entries[0].tags == ["projectA", "clientX"]

def test_count_time_by_tag():
    csv_file = create_temp_csv_file(CSV_CONTENT)
    entries = load_entries_from_csv(csv_file)
    time_counter = count_time_by_tag(entries)

    assert isinstance(time_counter, Dict)
    assert time_counter.get("projectA") == 105
    assert time_counter.get("projectB") == 45
    assert time_counter.get("clientX") == 90

def test_display_tag_and_time(capsys):
    time_counter = {"projectA": 105, "projectB": 45, "clientX": 90}
    display_tag_and_time(time_counter)

    captured = capsys.readouterr()
    output_lines = captured.out.split('\n')

    output_lines = [line.strip() for line in output_lines]

    # Use a regular expression to check for the pattern 'TOTAL TIME' followed by any number of spaces and 'TAG'
    assert re.search(r'TOTAL TIME\s+TAG', output_lines[0]) is not None
    assert "-------------------------" in output_lines[1]
    assert "105  #projectA" in output_lines[2]
    assert "45  #projectB" in output_lines[3]
    assert "90  #clientX" in output_lines[4]
