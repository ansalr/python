class String:
    
    def emailExtract(self):
        emaillist=["gopikrishna@v2etechnologies.com","manikandan@yahoo.com","mohans@google.com","vinith@hotmail.com"]
        serProvider = []
        for email in emaillist:
            for i,j in enumerate(email):
                if j == '@':
                    serProvider.append(email[i+1:])
        print(serProvider)
        
object1 = String()
object1.emailExtract()