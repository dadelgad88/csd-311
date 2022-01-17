#Pytech Collection Queries-5.3

#import statements
from pymongo import MongoClient

#MongoDB Connection String 
url = 'mongodb+srv://admin:admin@cluster0.azxqx.mongodb.net/t\pytech'

# connect to the MongoDB cluster
client = MongoClient(url)

# connect pytech database
db =client.pytech

#start of three students documents. 
#Izzy Chavez data document
Isaac = {
    "student_id": "1007",
    "first_name": "Isaac",
    "last_name": "Chavez",

}

# Maria Blackmon data document
Maria = {
    "student_id": "1008",
    "first_name": "Maria",
    "last_name": "Zapata",
}

Antonio = {
    "student_id": "1009",
    "first_name": "Antonio",
    "last_name": "Reyes",
}

#get the students collecion 
students = db.students

#insert statements with output 
print("\n --INSERT STATEMENTS --")

Isaac_student_id = students.insert_one(Isaac).inserted_id
print("  Inserted student record Isaac Chavez into the students collection with document_id " + str(Isaac_student_id))


Maria_student_id = students.insert_one(Maria).inserted_id
print("  Inserted student record Maria Zapata into the students collection with document_id " + str(Maria_student_id))


Antonio_student_id = students.insert_one(Antonio).inserted_id
print("  Inserted student record Antonio Reyes into the students collection with document_id " + str(Antonio_student_id))

input("\n\n  End of program, press any key to exit... ")
