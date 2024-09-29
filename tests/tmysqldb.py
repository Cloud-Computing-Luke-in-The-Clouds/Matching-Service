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
    context = dict(user="admin", password="lukeintheclouds",
                   host="user-profile.cxq2u204yw2o.us-east-1.rds.amazonaws.com", port=3306)
    data_service = MySQLRDBDataService(context=context)
    return data_service

def t1():
    data_service = get_db_service()
    data_service._get_connection()

if __name__ == '__main__':
    t1()