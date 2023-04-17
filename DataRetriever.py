"""
DataRetriever_v1.0: A simple python script which does the following:
    - Connects to DummyAPI.io and retrieves 10 user profile previews and extracts their id's into a list
    - It then generates links to each full profile and sends a request to each one
    - The data is iterated and the needed information is extracted
    - The script then calculates the length of each first name
    - It then connects to a MySQL database running on localhost in a docker container
    - And finally the data is imported into the database into the corresponding tables
"""

import requests
import mysql.connector

url_list = "https://dummyapi.io/data/v1/user?limit=10"
headers = {
    "app-id": "64370b141be40f574fa3a790"  # Replace with your own app ID
}

params = {
    "limit": 10
}

response = requests.get(url_list, headers=headers, params=params)
id_data = response.json()

user_ids = []
for user in id_data["data"]:
    user_id = user["id"]
    if user["title"] == "mr":
        user_ids.append(user_id)

base_url = "https://dummyapi.io/data/v1/user/"

headers = {
    "app-id": "64370b141be40f574fa3a790"
}

params = {
    "limit": 10
}

for user_id in user_ids:
    url_profile = base_url + user_id
    response = requests.get(url_profile, headers=headers, params=params)
    data = response.json()

    first_name = data["firstName"]
    last_name = data["lastName"]
    gender = data["gender"]
    dob = data["dateOfBirth"]
    first_name_length = len(first_name)

    print(first_name, last_name, gender, dob)
    print(f"The name {first_name} contains {first_name_length} characters.")

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@uthenticateUser13"
    )

    cur = mydb.cursor()
    cur.execute("USE USER_DB")

    sql_stmt = f"INSERT INTO User_Profiles(First_name, last_name, gender, dob, name_character_count) VALUES('{first_name}', '{last_name}', '{gender}', '{dob}', '{first_name_length}')"
    cur.execute(sql_stmt)
    mydb.commit()
    cur.close()
    mydb.close()




