"""
main.py
Main driver program for Student Performance & Attendance Analysis.
"""

import pandas as pd
import numpy as np
from functions import process_student_data

def print_separator(title: str = ""):
    print("\n" + "=" * 70)
    if title:
        print(f" {title.upper()} ".center(70, "="))
        print("=" * 70)

def main():
    # ---------------------------------------------------------
    # STEP 1: Read the Data
    # ---------------------------------------------------------
    csv_file = "students.csv"
    try:
        raw_df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: {csv_file} not found. Please ensure the CSV file is in the root directory.")
        return

    print_separator("Step 2: Dataset Overview")
    print(f"Total Records: {len(raw_df)}")
    print(f"Total Columns: {len(raw_df.columns)}")
    print(f"Columns: {', '.join(raw_df.columns)}")
    print("\nFirst 5 Records:")
    print(raw_df.head())

    # ---------------------------------------------------------
    # STEP 2: Process the Data
    # ---------------------------------------------------------
    subject_columns = ['Math', 'Science', 'English', 'History']
    processed_df = process_student_data(raw_df, subject_columns)

    print_separator("Step 3: Processed Student Records")
    display_cols = ['StudentID', 'Name', 'Total_Marks', 'Average_Marks', 'Grade', 'Attendance', 'Status']
    print(processed_df[display_cols].to_string(index=False))

    # ---------------------------------------------------------
    # STEP 3: Perform Analysis
    # ---------------------------------------------------------
    # 1. Highest scoring student
    top_student_idx = processed_df['Average_Marks'].idxmax()
    top_student = processed_df.loc[top_student_idx]

    # 2. Subject averages
    subject_averages = processed_df[subject_columns].mean().round(2)
    best_subject = subject_averages.idxmax()
    best_subject_avg = subject_averages.max()

    # 3. Pass / Fail counts
    pass_count = (processed_df['Status'] == 'Pass').sum()
    fail_count = (processed_df['Status'] == 'Fail').sum()
    pass_percentage = (pass_count / len(processed_df)) * 100

    # 4. Overall class average
    overall_class_avg = round(processed_df['Average_Marks'].mean(), 2)

    # 5. Attendance statistics
    avg_attendance = round(processed_df['Attendance'].mean(), 2)

    # ---------------------------------------------------------
    # STEP 4: Final Output & Summary Report
    # ---------------------------------------------------------
    print_separator("Step 4 & 5: Key Analytical Insights")
    print(f"1. Top Performing Student : {top_student['Name']} ({top_student['StudentID']})")
    print(f"   -> Average Marks       : {top_student['Average_Marks']}% (Grade: {top_student['Grade']})")
    print("-" * 70)
    print(f"2. Best Performing Subject: {best_subject} (Average: {best_subject_avg} / 100)")
    print(f"   Subject Average Breakdown:")
    for subj, avg in subject_averages.items():
        print(f"     - {subj:<10}: {avg}")
    print("-" * 70)
    print(f"3. Class Pass/Fail Summary:")
    print(f"   -> Total Passed        : {pass_count} / {len(processed_df)} ({pass_percentage:.1f}%)")
    print(f"   -> Total Failed        : {fail_count} / {len(processed_df)}")
    print("-" * 70)
    print(f"4. Overall Class Average  : {overall_class_avg} / 100")
    print(f"5. Average Attendance     : {avg_attendance}%")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()