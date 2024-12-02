def read_reports(file_path):
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by spaces and convert to integers
            report = list(map(int, line.split()))
            reports.append(report)
    return reports

def is_safe_report(report):
    # Check if the report is either all increasing or all decreasing
    is_increasing = True
    is_decreasing = True
    
    # Check differences between adjacent numbers
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        
        # Check if the difference is between 1 and 3 (inclusive)
        if not (1 <= abs(diff) <= 3):
            return False
        
        # Check if the sequence is increasing or decreasing
        if diff < 0:
            is_increasing = False
        if diff > 0:
            is_decreasing = False
    
    # A report is safe if it is either all increasing or all decreasing
    return is_increasing or is_decreasing

def is_safe_by_removing_one(report):
    # Try removing each level one by one to check if the sequence becomes safe
    for i in range(len(report)):
        # Create a new report with one level removed
        new_report = report[:i] + report[i+1:]
        
        # If removing the level makes the report safe, return True
        if is_safe_report(new_report):
            return True
    
    # If no level removal results in a safe report, return False
    return False

def count_safe_reports(file_path):
    reports = read_reports(file_path)
    safe_count = 0
    safe_after_removal_count = 0
    
    # Iterate through each report
    for report in reports:
        # First check if the report is safe without any modification
        if is_safe_report(report):
            safe_count += 1
        # If not safe, check if removing one level makes it safe
        elif is_safe_by_removing_one(report):
            safe_after_removal_count += 1
    
    # Return both counts
    return safe_count, safe_after_removal_count

# File path to your reports
file_path = 'day2.txt'

# Calculate and print the number of safe reports and safe reports after removal
safe_reports, safe_reports_after_removal = count_safe_reports(file_path)
updated_safe_reports = safe_reports + safe_reports_after_removal
print(f"Safe reports: {safe_reports}")
print(f"Updated safe reports: {updated_safe_reports}")
