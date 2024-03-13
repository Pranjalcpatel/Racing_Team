# A mail is spamif it contains keywords ahown in program below. Identify if the input email is spam or not.
spamlist=["buy now","click this","make a lot of money","subscribe now"]
email=input("Enter mail : ").lower()
found=0
for i in range (4):
    if(spamlist[i]) in email:
        found=1
        break
if(found==1): print("SPAM")
else: print("NOT SPAM")