"""
Module for generating a time utilization report based on data from a CSV file.

The CSV file should have three columns: 'desc', 'time', and 'tags'. 'desc' represents the task description,
'time' is the task duration in minutes (an integer), and 'tags' is a space-separated list of tags.
Tags are used to categorize tasks by projects, clients, or other criteria.

The program accepts the path to the CSV file as a command-line argument and displays a report.
Each line of the report corresponds to a tag, and it shows the total time spent on tasks with that tag.

"""
# python3 "Praktyczny_python_M06/Projekt 6.py" "Praktyczny_Python/M06/track.csv"

import click
import csv
from typing import Dict, List

class Entry:
    """
    Class representing a task entry.

    Attributes:
        desc (str): The description of the task.
        time (int): The duration of the task in minutes.
        tags (List[str]): A list of tags associated with the task.
    """
    def __init__(self, desc: str, time: int, tags: List[str]):
        self.desc = desc
        self.time = time
        self.tags = tags

    def __repr__(self) -> str:
       return f"(desc='{self.desc!r}', time={self.time!r}, tags={self.tags!r})"

def load_entries_from_csv(filename: str) -> List[Entry]:
    """
    Load task entries from a CSV file and return a list of Entry objects.

    Args:
        filename: Path to the CSV file.

    Returns:
        A list of Entry objects representing the task entries.
    """
    list_of_entries = []
    with open(filename) as stream:
        reader = csv.DictReader(stream)  
        for row in reader:  
            desc = row['desc']
            time = int(row['time'])
            tags = row['tags'].split()
            entry = Entry(desc, time, tags)
            print(entry)
            list_of_entries.append(entry)
        # print(list_of_entries)
        return list_of_entries

def count_time_by_tag(list_of_entries: List[Entry]) -> Dict[str, int]:
    """
    Count the total time for each tag in the given list of entries.

    Args:
        list_of_entries: A list of Entry objects representing the task entries.

    Returns:
        A dictionary where the keys are tags and the values are the total time spent on tasks with that tag.
    """
    time_counter = {}
    for entry in list_of_entries:
        tags = entry.tags  
        time = entry.time
        for tag in tags:
            if tag in time_counter:
                time_counter[tag] += time
            else:
                time_counter[tag] = time
    return time_counter
    
def display_tag_and_time(time_counter: Dict[str, int]) -> None:
    """
    Display the tag and corresponding total time in a formatted table.

    Args:
        time_counter: A dictionary where the keys are tags and the values are the total time spent on tasks with that tag.
    """
    print(f"{'TOTAL TIME':>12s}  {'TAG'}")
    print("-------------------------")
    for tag,time in time_counter.items():
        print(f"{str(time):>12s}  #{tag}")

@click.command()
@click.argument('csv_file')    
def main(csv_file: str) -> None:
    """
    Main entry point of the program.

    Args:
        csv_file: Path to the CSV file containing task entries.
    """
    list = load_entries_from_csv(csv_file)
    list_with_counter_and_time = count_time_by_tag(list)
    display_tag_and_time(list_with_counter_and_time)
  
if __name__ == '__main__':
    main()
