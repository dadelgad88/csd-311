
#import statements 
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.azxqx.mongodb.net/t\pytech"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
    
# update student_id 1007, 1008, 1009
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Chavez II"}})
result = students.update_one({"student_id": "1008"}, {"$set": {"last_name": "Zapata II"}})
result = students.update_one({"student_id": "1009"}, {"$set": {"last_name": "Reyes II"}})

# find the updated student documents for 1007,1008,1009
Isaac = students.find_one({"student_id": "1007"})
Maria = students.find_one({"student_id": "1008"})
Antonio = students.find_one({"student_id": "1009"})

# display message for 1007, 1008, 1009
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")
print("\n  -- DISPLAYING STUDENT DOCUMENT 1008 --")
print("\n  -- DISPLAYING STUDENT DOCUMENT 1009 --")

# output the updated document to the terminal window
print("  Student ID: " + Isaac["student_id"] + "\n  First Name: " + Isaac["first_name"] + "\n  Last Name: " + Isaac["last_name"] + "\n")
print("  Student ID: " + Maria["student_id"] + "\n  First Name: " + Maria["first_name"] + "\n  Last Name: " + Maria["last_name"] + "\n")
print("  Student ID: " + Antonio["student_id"] + "\n  First Name: " + Antonio["first_name"] + "\n  Last Name: " + Antonio["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
