import csv

department_employees = {}
department_total_score = {}
department_total_training = {}
department_avg_training = {}
total_employees = 0
no_total_training = 0

with open("hr_data.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_employees += 1
        department = row["department"]
        avg_training_score = int(row["avg_training_score"])
        no_of_training = float(row["no_of_trainings"])

        if department not in department_employees:
            department_employees[department] = 1
        else:
            department_employees[department] += 1
            no_total_training += no_of_training
            
        
        if department not in department_total_score:
            department_total_score[department] = avg_training_score
        else:
            department_total_score[department] += avg_training_score
        
        if department not in department_total_training:
            department_total_training[department] = no_of_training
        else:
            department_total_training[department] += no_of_training

        for department in department_total_training:
            department_avg_training[department] = department_total_training[department] / department_employees[department]

department_summary = []

for department in department_employees:
    count = department_employees[department]
    total_score = department_total_score[department]
    average_score = total_score / count
    department_summary.append((department, count, round(average_score, 2)))
    #department_summary.sort(key=lambda x: x[2], reverse=True)
    #best_department = department_summary[0]

print(f"Il numero totale dei dipendenti è: {total_employees}\n")

print(f"{'Department':<20} {'Employees':<10} {'Avg Score':<10} {'Performance':<15} {'AVG no of training':<20}")
print("-" * 80)

for dep, count, avg in department_summary:
    # Since training scores are on a 0–100 scale, 
    # I considered values below 60 as indicative of weak performance.
    if avg < 60:
        label = "Low"
    elif avg < 75:
        label = "Medium"
    else:
        label = "High"
    print(f"{dep:<20} {count:<10} {avg:<10} {label:<15} {department_avg_training[dep]:<20.2f}")
