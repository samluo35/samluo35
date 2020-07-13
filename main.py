username = input("What is your username? ")
age = input("How old are you " + username + "? " )
if int(age) < 13:
  print("Sorry " + username + ", you are not old enough to create an account yet.") 
elif int(age) > 99:
  print("Are you sure you are above the age of 99?")
else:
  print("You have successfully created your account" ) 