#given a string find whether it is a valid 10-digit number 
phno = "234-456-9999"
length =len(phno)
if length == 12 \
   and phno[3] == "-" \
   and phno[7] == "-" \
   and phno[:3].isdigit() \
   and phno[4:7].isdigit() \
   and phno[8:].isdigit():
    print("valid phone number")
else:
    print("Invalid phone number")
