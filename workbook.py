def dictionary():  
    std_detial = [
        {"name":"jack" ,"house": "Griffindor","patronus":"otter" },
        {"name": "Robert","house": "Griffindor","patronus":"stag" },
        {"name": "Herbert","house": "Griffindor","patronus": "russel"},
        {"name": "arun","house": "Slytherin","patronus": None},
    ]
    
   
    for details in std_detial:  

        if "jack" == details["name"]:
            print(details,details["name"],details["house"],details["patronus"],sep="\n")
            keys = details.keys()
            print(keys)

dictionary()