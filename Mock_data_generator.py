import json
import random

name_list = ["Shashank","Amit","Nitin","Manish","Nikhil","Kunal","Vishal"]
age_list = [29,34,21,23,27,22,20]
salary_list = [1000,2000,3000,4000,5000,6000,7000]

def lambda_handler(event, context):
    # TODO implement
    random_index = random.randint(0,6)
    mock_data = {}
    mock_data['emp_name'] = name_list[random_index]
    mock_data['emp_age'] = age_list[random_index]
    mock_data['emp_salary'] = salary_list[random_index]
    return mock_data
