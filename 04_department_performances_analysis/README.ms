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

The following steps were implemented using Python:

* Data parsing from CSV file
* Aggregation by department:

  * Total number of employees
  * Average performance score
  * Average number of trainings
* Department classification based on performance:

  * **Low**: score < 60
  * **Medium**: 60 <= score < 75
  * **High**: score >= 75
* Tabular reporting with formatted output
* Comparative analysis between training frequency and performance

---

## Key Findings

* Departments with **low training frequency** tend to show **lower performance**, suggesting that training may have a positive impact.
* However, the **Sales & Marketing department** represents a notable exception:

  * High average number of trainings
  * Low performance score

This indicates that training quantity alone is **not sufficient** to explain performance differences.

---

## Insights

The analysis suggests that:

* Training frequency is **not a strong standalone predictor** of performance
* The relationship between training and performance is **non-linear and context-dependent**
* Some departments may benefit from training, while others do not.

Possible explanations include:

* Ineffective or low-quality training programs
* Misalignment between training content and job requirements
* Information overload due to excessive training
* External factors (e.g., workload, experience level, turnover)

---

## Business Recommendations

Based on the findings, the following actions are recommended:

1. **Review training effectiveness**
   Evaluate whether training content is relevant and practical.

2. **Customize training by department**
   Avoid a one-size-fits-all approach.

3. **Measure training impact**
   Introduce KPIs to assess training outcomes.

4. **Investigate underperforming departments**
   Conduct qualitative analysis (e.g., interviews, feedback).

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

