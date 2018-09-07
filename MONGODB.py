'''
Q.1- Write a python script to create a databse of students named Students.
Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
Q.4- Print the names of all the students who scored more than 80 marks.
'''

import pymongo
client=pymongo.MongoClient()
database=client['Students']
print('STUDENTS DATABASE CREATED')
collection=database['Student Data']
print('STUDENTS DATA TABLE CREATED')
for i in range (1,11):
    print('Enter Detail Of Student {}:'.format(i))
    name=input('Name:')
    marks=int(input('Marks:'))
    collection.insert_one({'Name':name,'Marks':marks})
print('VALUES INSERTED')
data=collection.find({'Marks':{"$gt" : 80}})
for details in data:
    print('MARKS GREATER THAN 80',details)


