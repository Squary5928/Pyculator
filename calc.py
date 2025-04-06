import os
os.system('clear')
while True:
 print("Choose the number according to your choice,")
 print("\n1) Multiplication")
 print("2) Division")
 print("3) Addition")
 print("4) Subtraction")
 print("5) Exit")
 choice = input("\nWhich option do you want to choose?: ")
 if choice == "1":
  os.system('clear')
  a = int(input("First number: "))
  b = int(input("Second number: "))
  ans = a*b
  print(ans, "is your answer.")
  ch = input("Do you want to open calculator again (any key) or exit (e)?: ")
  if ch == "e":
   os.system('clear')
   break
  else:
   os.system('clear')
 elif choice == "2":
  os.system('clear')
  a = int(input("First number: "))
  b = int(input("Second number: "))
  if b != 0:
   ans = a/b
   print(ans, "is your answer.")
  else:
   print("Error: Cannot divide by zero!")
  ch = input("Do you want to open calculator again (any key) or exit (e)?: ")
  if ch == "e":
   os.system('clear')
   break
  else:
   os.system('clear')
 elif choice == "3":
  os.system('clear')
  a = int(input("First number: "))
  b = int(input("Second number: "))
  ans = a+b
  print(ans, "is your answer.")
  ch = input("Do you want to open calculator again (any key) or exit (e)?: ")
  if ch == "e":
   os.system('clear')
   break
  else:
   os.system('clear')
 elif choice == "4":
  os.system('clear')
  a = int(input("First number: "))
  b = int(input("Second number: "))
  ans = a-b
  print(ans, "is your answer.")
  ch = input("Do you want to open calculator again (any key) or exit (e)?: ")
  if ch == "e":
   os.system('clear')
   break
  else:
   os.system('clear')
 if choice == "5":
  print("Exiting calculator, goodbye!")
  os.system('sleep 1')
  os.system('clear')
  break

else:
  os.system('clear')
  print("")
  print("Invalid choice! Choose 1, 2, 3, 4, or 5.")

