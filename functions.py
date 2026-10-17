"""
functions.py
Utility functions for calculating grades, pass/fail status, and student metrics.
"""

import numpy as np
import pandas as pd

def determine_grade(average_score: float) -> str:
    """Assign letter grade based on overall average."""
    if average_score >= 90:
        return 'A+'
    elif average_score >= 80:
        return 'A'
    elif average_score >= 70:
        return 'B'
    elif average_score >= 60:
        return 'C'
    elif average_score >= 40:
        return 'D'
    else:
        return 'F'

def check_pass_status(row: pd.Series, subject_cols: list, passing_mark: int = 40) -> str:
    """
    A student passes only if they score >= passing_mark in all subjects
    and maintain at least 60% attendance.
    """
    passed_all_subjects = all(row[col] >= passing_mark for col in subject_cols)
    attendance_ok = row['Attendance'] >= 60
    return "Pass" if (passed_all_subjects and attendance_ok) else "Fail"

def process_student_data(df: pd.DataFrame, subject_cols: list) -> pd.DataFrame:
    """
    Computes total marks, averages, grades, and status using Pandas and NumPy.
    """
    processed_df = df.copy()

    # Vectorized computation using NumPy / Pandas
    processed_df['Total_Marks'] = processed_df[subject_cols].sum(axis=1)
    processed_df['Average_Marks'] = np.round(processed_df[subject_cols].mean(axis=1), 2)
    
    # Apply grading rule
    processed_df['Grade'] = processed_df['Average_Marks'].apply(determine_grade)
    
    # Apply pass/fail check
    processed_df['Status'] = processed_df.apply(
        lambda row: check_pass_status(row, subject_cols), axis=1
    )
    
    return processed_df