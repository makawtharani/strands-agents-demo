import csv
import os
from datetime import datetime

def log_to_csv(application_type: str, event_id: str, **kwargs):
    """Log application details to CSV file"""
    csv_file = "applications.csv"
    file_exists = os.path.isfile(csv_file)
    
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        if not file_exists:
            # Write header if file doesn't exist
            if application_type == "speaker":
                fieldnames = ['timestamp', 'type', 'event_id', 'name', 'topic']
            else:  # sponsor
                fieldnames = ['timestamp', 'type', 'event_id', 'company', 'tier']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
        
        # Write the application data
        row_data = {
            'timestamp': datetime.now().isoformat(),
            'type': application_type,
            'event_id': event_id,
            **kwargs
        }
        
        if application_type == "speaker":
            fieldnames = ['timestamp', 'type', 'event_id', 'name', 'topic']
        else:  # sponsor
            fieldnames = ['timestamp', 'type', 'event_id', 'company', 'tier']
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(row_data) 