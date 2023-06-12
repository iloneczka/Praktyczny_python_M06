# Napisz własną analitykę do aplikacji do śledzenia czasu takich jak np. Toggl Track. Twój moduł wczytuje dane o czasie wykonania poszczególnych zadań w formacie CSV, a następnie generuje raport wykorzystania czasu z podziałem na projekty, klientów i inne tagi.

# 1. Dane w pliku CSV mają trzy kolumny: desc, time oraz tags. Desc jest opisem zadania. Time to liczba całkowita określająca czas wykonywania tego zadania w minutach. Natomiast tags jest listą tagów porozdzielanych spacjami. Jedno zadanie może mieć wiele tagów. Jednym tagiem może być otagowane wiele zadań. Tagi służą do oznaczania zadań wg projektów, klientów lub innych kryteriów.

# 2. Upakuj te trzy informacje w klasie Entry. Upewnij się, że ma ona metodę __repr__.

# 3. Program przyjmuje scieżkę do pliku CSV jako argument linii poleceń. Następnie wyświetla raport. Każda jego linia to jeden tag. Dla każdego tagu wyliczona jest suma wszystkich otagowanych nim zadań.

# 4. Nie musisz pisać testów, ale podziel program na funkcje tak, aby każda z nich robiła tylko jedną rzecz.

import csv

class Entry:
    def __init__(self, desc, time, tags):
        self.desc = desc
        self.time = time
        self.tags= tags

    def __repr__(self):
       return f"POMIDOR(desc='{self.desc!r}', time={self.time!r}, tags={self.tags!r})"
    
    def __str__(self):
        return self.__repr__()

def load_entries_from_csv(filename):
    list_of_entries= []
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

# def edit_by_tags(list_of_entries):
#     tags_= {}
#     for entry in list_of_entries:


def main():
    FILENAME= "/Users/ilo/Desktop/PYTHON/Praktyczny_Python/M06/track.csv"
    list= load_entries_from_csv(FILENAME)
    print(list)




if __name__ == '__main__':
    main()
