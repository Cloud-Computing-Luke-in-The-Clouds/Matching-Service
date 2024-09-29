import os
import sys
import subprocess

# Try to find 'framework' in parent directories
current_dir = os.getcwd()
while current_dir != '/':
    if os.path.exists(os.path.join(current_dir, 'framework')):
        print(f"Found 'framework' in: {current_dir}")
        sys.path.append(current_dir)
        break
    current_dir = os.path.dirname(current_dir)

# Try to import the required module
try:
    from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService
    print("Successfully imported MySQLRDBDataService")
except ImportError as e:
    print(f"Import error: {e}")
    print("Couldn't import MySQLRDBDataService. Check if the 'framework' directory is in the correct location.")

import json

def get_db_service():
    context = dict(user="root", password="dbuserdbuser",
                   host="localhost", port=3306)
    data_service = MySQLRDBDataService(context=context)
    return data_service

def t1():
    data_service = get_db_service()
    result = data_service.get_data_object(
        "course_management",
        "course_sections",
        key_field="sis_course_id",
        key_value="COMSW4153_001_2024_3"
    )
    print("t1 result = \n", json.dumps(result, indent=4, default=str))

if __name__ == '__main__':
    t1()