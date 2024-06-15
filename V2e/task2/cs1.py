class String:
    
    def count(self,substring = input()):
        string =  """Your service may continue to run for a brief period, but to ensure
 uninterrupted service, you need to update the expiry date or add another
 primary card to avoid cancel your service. Please note that any outstanding
 balance may be charged within 24 hours of you updating your payment
 method to continue your service."""
        
        output = string.count(substring)
        print(output)
        
        
str1 = String()
str1.count()