import pandas as pd
from django.shortcuts import render
import os

# Define the path to the CSV files directory
CSV_DIR = '/Users/macbook/Desktop/Ganison_dataset'

def read_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f'File not found: {file_path}')
        return pd.DataFrame()  # Return an empty DataFrame

def combine_student_data():
    csv_files = [
        'Ganison_dataset_1.csv',
        'Ganison_dataset_2.csv',
        'Ganison_dataset_3.csv',
        'Ganison_dataset_4.csv',
        'Ganison_dataset_5.csv',
        'Ganison_dataset_6.csv'
    ]
    
    dataframes = []
    
    for file in csv_files:
        file_path = os.path.join(CSV_DIR, file)
        print(f"Loading file: {file_path}")  # Print the file path for debugging
        try:
            df = read_csv(file_path)
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
    
    combined_df = pd.concat(dataframes, ignore_index=True)
    student_columns = [
        'school_name', 'year', 'StudentID', 'First Name', 'Last Name', 
        'Year Level', 'Class', 'Subject', 'Answers', 'Correct Answers',
        'correct_answer_percentage_per_class', 'average_score', 'school_percentile',
        'sydney_percentile', 'strength_status', 'high_distinct_count', 'distinct_count',
        'credit_count', 'participant_count', 'award'
    ]
    student_df = combined_df[student_columns]
    
    return student_df


def table_view(request, table_name):
    if table_name == 'student':
        # Combine student data from all CSV files
        student_df = combine_student_data()
        
        # Rename columns to avoid spaces
        student_df.columns = [col.replace(' ', '_') for col in student_df.columns]
        
        # Create the Full Name column by concatenating First Name and Last Name
        student_df['Full_Name'] = student_df['First_Name'] + ' ' + student_df['Last_Name']
        
        # Select only the relevant columns for display
        student_df_filtered = student_df[['StudentID', 'Full_Name']].drop_duplicates()
        
        # Convert the DataFrame to a dictionary for rendering
        data = student_df_filtered.to_dict(orient='records')
        
        # Render the student table template
        return render(request, 'student.html', {'data': data})
    
    # Handle other table views (if needed)
    return render(request, '404.html', {'message': 'Table not found.'})

