# Time Utilization Report Generator

This Python program generates a time utilization report based on data from a CSV file. The CSV file should have three columns: 'desc', 'time', and 'tags'. 'desc' represents the task description, 'time' is the task duration in minutes (an integer), and 'tags' is a space-separated list of tags. Tags are used to categorize tasks by projects, clients, or other criteria.

## Table of Contents
- [General Info](#general-info)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Testing](#testing)
- [Solutions](#solutions)
- [Future Plans](#future-plans)
- [Inspirations and Acknowledgments](#inspirations-and-acknowledgments)


## General Info
This program processes a CSV file containing task entries and generates a report showing the total time spent on tasks for each tag.

## Technologies Used
The program is written in Python.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Prerequisites
To run this project, make sure you have Python 3.x installed on your computer and the required libraries.  
If you haven't installed the click library yet, you can do so by running:
```
pip install click
```

## Setup
To run the project locally, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.

### Usage
To generate the time utilization report, follow these steps:

1. Prepare a CSV file with the following columns: 'desc', 'time', and 'tags'.
2. Run the program:
```
python3 "time_utilization_report_generator.py" "path/to/your/csv/file.csv"
```
The program will process the CSV file and display the time utilization report, grouping tasks by tags and showing the total time spent on each tag.

## Testing

TODO

## Solutions
The module consists of the following components:

1. Entry Class

The `Entry` class represents a task entry with the following attributes:

* `desc` (str): The description of the task.
* `time` (int): The duration of the task in minutes (an integer).
* `tags` (List[str]): A list of tags associated with the task.

2. `load_entries_from_csv` Function

This function loads task entries from a CSV file and returns a list of `Entry` objects.

3. `count_time_by_tag` Function

This function counts the total time for each tag in the given list of entries.

4. `display_tag_and_time` Function

This function displays the tag and corresponding total time in a formatted table.

5. `main` Function

The main entry point of the program that utilizes the above functions to generate the time utilization report.

## Future Plans
This project was inspired by the "Praktyczny Python" training course and was adapted from the original version for educational purposes.
The module can be enhanced with additional features like:

Filtering tasks by date range
Sorting the report by total time spent
Exporting the report to different formats (e.g., PDF, Excel)

## Inspirations and Acknowledgments
This project was inspired by the "Praktyczny Python" training course and was adapted from the original version for educational purposes.
