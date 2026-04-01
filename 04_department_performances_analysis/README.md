#  HR Data Analysis – Department Performance & Training Evaluation

## Project Overview

This project analyzes an HR dataset to evaluate employee performance across departments and investigate whether training frequency impacts performance outcomes.
The goal is to identify patterns, detect anomalies, and derive actionable business insights that could support decision-making in a real organizational context.

---

## Dataset Description

The dataset contains employee-level information, including:

* **Department** – Department the employee belongs to
* **Avg Training Score** – Performance score (0–100 scale)
* **Number of Trainings** – Number of training sessions attended

---

## Analysis Performed

The analysis was carried out using Python, starting from raw CSV data and progressively transforming it into meaningful insights.
First, the dataset was parsed and cleaned to extract the relevant variables for each employee. The data was then grouped by department in order to compute key metrics such as the number of employees, the average performance score, and the average number of trainings attended.
Departments were subsequently classified into three categories (Low, Medium, High) based on their average performance score. This made it easier to compare groups and identify patterns.

Finally, the results were organized into a structured table, allowing for a direct comparison between training frequency and performance across departments.

---

# Results summary

The table below shows the aggregated results by department:

| Department         | Employees | Avg Score | Performance | Avg Trainings |
|--------------------|-----------|-----------|-------------|---------------|
| Analytics          | 2319      | 84.54     | High        | 1.35          |
| R&D                | 440       | 84.41     | High        | 1.35          |
| Technology         | 3011      | 79.86     | High        | 1.25          |
| Procurement        | 3020      | 70.15     | Medium      | 1.34          |
| Finance            | 1091      | 60.32     | Medium      | 1.31          |
| Operations         | 4764      | 60.30     | Medium      | 1.17          |
| Legal              | 445       | 59.58     | Low         | 1.08          |
| HR                 | 1085      | 50.31     | Low         | 1.07          |
| Sales & Marketing  | 7315      | 50.09     | Low         | 1.27          |

---

## Key Findings

The analysis reveals a mixed relationship between training frequency and performance.
Departments with lower training exposure generally tend to have lower performance scores, suggesting that training may play a role in improving outcomes. However, this relationship is not consistent across all departments.
In particular, Sales & Marketing stands out as an exception: despite having a relatively high average number of trainings, it shows one of the lowest performance scores. This suggests that simply increasing the number of training sessions is not sufficient.

---

## Insights

These results suggest that the effectiveness of training is likely more important than its frequency.
While training appears to be beneficial in some departments, its impact varies significantly depending on context. Factors such as training quality, relevance to job roles, and employee engagement may play a crucial role.
Additionally, the presence of outliers indicates that other variables - such as workload, experience, or organizational dynamics - may influence performance.

---

## Business Recommendations

Rather than increasing the number of training sessions across the board, organizations should focus on improving the quality and relevance of training programs.
In particular, departments such as Sales & Marketing should be analyzed more closely to understand why high training exposure does not translate into better performance.
A more targeted approach - including feedback collection, performance tracking, and tailored training paths - could lead to more effective outcomes.

---

## Technologies Used

* Python
* CSV data handling ('csv' module)
* Dictionaries for aggregation
* Basic statistical analysis

---

## Future Improvements

* Add data visualization (e.g., matplotlib)
* Compute correlation between variables
* Use pandas for more advanced analysis
* Build a dashboard for interactive insights

---

## Sintesi (Italiano)

L'analisi evidenzia che il numero di training non è sufficiente a spiegare le performance dei dipartimenti. Sebbene una bassa frequenza di training sia associata a risultati peggiori, esistono eccezioni significative (come Sales & Marketing), che suggeriscono che l'efficacia e la qualità dei training siano fattori più rilevanti della quantità.

