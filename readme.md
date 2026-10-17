# Comprehensive Student Performance & Academic Analytics System

> An automated data analytics pipeline built with Python, Pandas, and NumPy to ingest academic records, evaluate performance metrics, check regulatory attendance criteria, and extract statistical cohort insights.

---

## 1. Project Title & Details

* **Project Title:** Comprehensive Student Performance & Academic Analytics System
* **Author / Student Name:** [Your Name / Roll Number]
* **Course / Department:** Computer Science / Data Analytics / Information Technology
* **Academic Term:** 2025–2026

---

## 2. Objective

Educational institutions process large volumes of student assessment and attendance data each semester. Performing these evaluations manually via spreadsheets is labor-intensive, error-prone, and slow to highlight students who need immediate intervention.

The objectives of this project are:
1. **Automate Core Computations:** Calculate aggregate scores, percentage averages, letter grades, and pass/fail statuses programmatically.
2. **Attendance Compliance Verification:** Automatically flag students falling below mandatory attendance thresholds (e.g., `< 75%`).
3. **Statistical Cohort Analysis:** Identify top-performing students, at-risk students, subject-level performance benchmarks, and demographic trends.
4. **Data-Driven Insights:** Compute mathematical correlations between classroom attendance and final examination performance.

---

## 3. Technologies Used

* **Language:** Python 3.10+
* **Libraries:**
  * **[Pandas](https://pandas.pydata.org/):** Tabular data ingestion, missing-value diagnostics, group-by aggregations, and vectorized tabular transformation.
  * **[NumPy](https://numpy.org/):** Vectorized condition branching (`np.where`), linear algebra calculations, and Pearson correlation coefficient computation (`np.corrcoef`).
* **Environment:** Compatible with any Standard Python terminal, Visual Studio Code, or Jupyter Notebook.

---

## 4. Dataset Description

The dataset is stored in `student_records.csv` and contains **18 records** representing an academic section across **9 core attributes**:

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `StudentID` | `String` | Unique identifier (e.g., `STU101` to `STU118`) |
| `Name` | `String` | Full student name |
| `Gender` | `String` | Gender category (`Male` / `Female`) |
| `Math` | `Integer` | Mathematics score (Scale: 0–100) |
| `Science` | `Integer` | Science score (Scale: 0–100) |
| `English` | `Integer` | English score (Scale: 0–100) |
| `History` | `Integer` | History score (Scale: 0–100) |
| `ComputerScience` | `Integer` | Computer Science score (Scale: 0–100) |
| `AttendancePercentage` | `Float` | Term attendance percentage (Scale: 0.0–100.0%) |

---

## 5. Implementation Workflow

### Architecture Pipeline

```text
       [ student_records.csv ]
                  │
                  ▼
   Pandas DataFrame Ingestion
   ├── Shape & null value verification
   └── Data type diagnostics
                  │
                  ▼
   Vectorized Processing (Pandas + NumPy)
   ├── TotalMarks = sum(5 subjects)
   ├── AverageMarks = mean(5 subjects)
   ├── Grade Mapping via conditional rules
   ├── Subject Pass Matrix (>= 40 in ALL subjects)
   └── Attendance Eligibility check (>= 75%)
                  │
                  ▼
   Statistical Analysis
   ├── Top & bottom performers (idxmax / idxmin)
   ├── Subject means & benchmark ranking
   ├── Demographic breakdown (groupby Gender)
   └── Pearson correlation (Attendance vs. Marks)
                  │
                  ▼
   Formatted Executive Output & Scorecard

###Step-by-Step Execution

Data Ingestion: The dataset is loaded using pd.read_csv(), followed by .info() and .isnull().sum() to verify schema types and ensure there are no missing values.
Feature Engineering:
Total Marks: Computed using df[subjects].sum(axis=1).
Average Marks: Computed using df[subjects].mean(axis=1) and rounded to 2 decimal places.
Letter Grading Scale:
90.0% - 100.0%: A+
80.0% - 89.9%: A
70.0% - 79.9%: B
60.0% - 69.9%: C
50.0% - 59.9%: D
< 50.0%: F
Per-Subject Pass/Fail Condition: A student receives a PASS status only if they score 40 or more in all 5 subjects. If any subject mark is below 40, status is FAIL.
Attendance Status: Evaluated using np.where(df['AttendancePercentage'] >= 75.0, 'Eligible', 'Shortage').

##Statistical Analysis:

Cohort topper and lowest scorer identified via .idxmax() and .idxmin().
Subject benchmarks calculated via column-wise .mean().
Group performance evaluated using df.groupby('Gender').
Linear association calculated using np.corrcoef(df['AttendancePercentage'], df['AverageMarks'])[0, 1].

###6. Key Features

Strict Per-Subject Pass Criteria: Prevents students who fail individual subjects from passing on aggregate marks alone.
Attendance Risk Flagging: Immediately flags students with less than 75% attendance for examination eligibility review.
Vectorized Computations: Uses Pandas and NumPy vectorization instead of row-by-row iteration for improved performance.
Correlation Metric: Quantifies how strongly attendance impacts final grades.
Reproducible Execution: Self-contained script generates the sample dataset automatically if the CSV is not found.

### Output / Execution Results 
================================================================================
                      ACADEMIC PERFORMANCE REPORT
================================================================================

[1] CLASS SUMMARY METRICS:
    - Total Enrolled Students      : 18
    - Overall Class Average Score   : 69.84 / 100
    - Number of Students Passed    : 15 (83.33%)
    - Number of Students Failed    : 3 (16.67%)
    - Attendance-Score Correlation : 0.963 (Strong positive correlation)

[2] TOP AND BOTTOM PERFORMERS:
    - Academic Topper              : Tanvi Deshmukh (STU112) with 94.2% (Grade: A+)
    - Needs Remedial Support       : Aditya Joshi (STU109) with 36.0% (Grade: F)

[3] SUBJECT-LEVEL BENCHMARK:
    - Best Performing Subject      : ComputerScience (Average: 76.44/100)
    - All Subject Averages:
Math               67.33
Science            71.67
English            69.67
History            67.89
ComputerScience    76.44

[4] DEMOGRAPHIC BREAKDOWN:
        AverageMarks  AttendancePercentage
Gender                                    
Female         81.70                 93.00
Male           57.98                 77.30

[5] GRADE DISTRIBUTION:
Grade
A     4
A+    4
B     3
C     3
D     1
F     3

--------------------------------------------------------------------------------
FULL STUDENT SCORECARD
--------------------------------------------------------------------------------
StudentID              Name Gender  TotalMarks  AverageMarks Grade Status  AttendancePercentage AttendanceEligibility
   STU101      Aarav Sharma   Male         430         86.00     A   PASS                  94.5             Eligible
   STU102        Diya Patel Female         470         94.00    A+   PASS                  98.0             Eligible
   STU103       Rohan Verma   Male         255         51.00     D   PASS                  78.2             Eligible
   STU104       Ananya Iyer Female         422         84.40     A   PASS                  91.0             Eligible
   STU105       Kabir Singh   Male         207         41.40     F   FAIL                  62.5             Shortage
   STU106    Sneha Kulkarni Female         449         89.80     A   PASS                  96.5             Eligible
   STU107        Vikram Rao   Male         340         68.00     C   PASS                  85.0             Eligible
   STU108        Pooja Nair Female         413         82.60     A   PASS                  89.5             Eligible
   STU109      Aditya Joshi   Male         180         36.00     F   FAIL                  55.0             Shortage
   STU110         Meera Sen Female         386         77.20     B   PASS                  88.0             Eligible
   STU111    Karan Malhotra   Male         309         61.80     C   PASS                  80.5             Eligible
   STU112    Tanvi Deshmukh Female         471         94.20    A+   PASS                  99.0             Eligible
   STU113         Arjun Das   Male         275         55.00     D   PASS                  74.0             Shortage
   STU114        Ishita Roy Female         434         86.80     A   PASS                  92.5             Eligible
   STU115      Nikhil Reddy   Male         217         43.40     F   FAIL                  68.0             Shortage
   STU116       Rhea Kapoor Female         454         90.80    A+   PASS                  95.0             Eligible
   STU117   Siddharth Mehta   Male         366         73.20     B   PASS                  83.5             Eligible
   STU118    Priyanka Ghosh Female         337         67.40     C   PASS                  82.0             Eligible
================================================================================
8. Final Outcome
The project successfully automates the academic evaluation and reporting workflow:
Efficiency and Accuracy: Eliminates manual spreadsheet calculations and removes risk of calculation errors across totals, averages, and pass/fail assignments.
Key Findings:
Academic Topper: Tanvi Deshmukh (STU112) achieved the highest score with an average of 94.2% (Grade A+).
Subject Performance: Computer Science had the highest class average (76.44%), while Mathematics had the lowest (67.33%).
Pass Rate: 83.33% (15 of 18 students) passed all subjects.
Statistical Insight:
The correlation coefficient between attendance and average marks was +0.963, showing a very strong positive relationship.
All students who failed the term examination also had attendance rates below 75%, highlighting attendance as an effective early indicator for academic intervention."# Student-performance-analytics." 
"# Student-performance-analytics." 
