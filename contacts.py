contacts ={ 
    "number":"4",
    "students": [
    {"name":"shravan", "email":"shravan@xyz.com"},
    {"name":"Kumar", "email":"kumar@xyz.com"},     
    {"name":"shrav", "email":"shrav@xyz.com"},
    {"name":"kum", "email":"kum@xyz.com"}
    ]
 } 

for student in contacts["students"]:
    print(student['email'])