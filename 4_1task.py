from pathlib import Path
import shutil

data = [("Korp", 3000), ("Borisenko", 2000), ("Raju", 1000)]


with open ("salaries.txt", "w") as fh:  
    for surname, salary in data:
        fh.write(f"{surname},{salary}\n")
        
def total_salary(path):
    salaries = []

    with open(path, "r") as fh:
        for line in fh:
            parts = line.strip().split(",")
            salary = int(parts[1])
            salaries.append(salary)

    total = sum(salaries)
    average = total / len(salaries)

    return total, average

result = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {result[0]}")
print(f"Середня заробітна плата: {result[1]}")