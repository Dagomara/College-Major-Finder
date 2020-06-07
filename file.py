print("I will try to guess what college major you will like the most.")
input("Press enter to start.")
print("\n\n\n")

all = {"Science": 0, "Math": 0, "History": 0, "Computer Science": 0, "English": 0, "Psychology": 0}

q = input("Are colons used to separate a dependent clause and an independent clause: ")
if (q.lower == "no"):
  all["English"] += 1
  print("Correct")

q = input("What is the square root of 121: ")
if (q == "11"):
  all["Math"] += 1
  print("Correct")

q = input("In what year did Christopher Columbus sail the ocean blue: ")
if (q == "1492"):
  all["History"] +=1
  print("Correct")

q = input("What statement is used to add a second condition to an if statement in Python: ")
if (q.lower() == "elif"):
  all["Computer Science"] += 1
  print("Correct")

q = input("What is the Freudian concept for the part of the mind where primal and instinctive urges manifest: ")
if (q.lower() == "id"):
  all["Psychology"] += 1
  print("Correct")

q = input("How many protons does carbon have: ")
if (q == "6"):
  all["Science"] += 1
  print("Correct")

q = input("What English mark always ends an interrogatory sentence: ")
if (q == "?"):
  all["English"] += 1
  print("Correct")

q = input("What is the derivative of 3x^3 + 4x^(1/2): ")
if (q == "9x^2 + 2x^(-1/2)" or q == "9x^2 + 2x^-1/2"):
  all["Math"] += 1
  print("Correct")

q = input("Who rang a bell to condition dogs to salivate: ")
if ("pavlov" in q.lower()):
  all["Psychology"] += 1
  print("Correct")

q = input("What country was blamed for the sinking of the USS Maine: ")
if (q == "Spain"):
  all["History"] +=1
  print("Correct")

q = input("What is the densest thing in the universe: ")
if (q.lower() == "black hole"):
  all["Science"] += 1
  print("Correct")

q = input("Who was the Northern general who served under Abraham Lincoln and eventually became president: ")
if ("grant" in q.lower()):
  all["History"] +=1
  print("Correct")

q = input("What is a learning technique that helps store and retrieve information in memory: ")
if (q.lower() == "mnemonic"):
  all["Psychology"] += 1
  print("Correct")
  
q = input("What is the rhetorical device that appeals to emotion: ")
if (q.lower() == "pathos"):
  all["English"] += 1
  print("Correct")

q = input("Would you use a for loop or a while loop when you want some code to run until a specific condition is met: ")
if ("while" in q.lower()):
  all["Computer Science"] += 1
  print("Correct")

q = input("What does ionizing radiation remove from atoms and molecules: ")
if ("electron" in q.lower()):
  all["Science"] += 1
  print("Correct")

q = input("What happened to Germany's economy after its defeat in World War 1: ")
if ("inflation" in q.lower()):
  all["History"] += 1
  print("Correct")

q = input("Who wrote the novel All My Sons: ")
if ("miller" in q.lower()):
  all["English"] += 1
  print("Correct")

q = input("What is another word for dihydrogen monoxide: ")
if (q.lower()=="water"):
  all["Science"] += 1
  print("Correct")

q = input("What does '==' mean: ")
if ("check" in q.lower() or "equal" in q.lower()):
  all["Computer Science"] += 1
  print("Correct")

q = input("If an object has a linear displacement graph with points (2.16, 7.21) and (0.34, 4.23), what is the acceleration of the object: ")
if (q == "0"):
  all["Math"] += 1
  print("Correct")

q = input("Which gender is Bipolar Disorder more common in: ")
if (q.lower() == "female"):
  all["Psychology"] += 1
  print("Correct")

q = input("Who was the second president of the USA: ")
if ("adams" in q.lower()):
  all["History"] += 1
  print("Correct")

q = input("What is the standard deviation of a normal curve: ")
if ("1" in q):
  all["Math"] += 1
  print("Correct")

q = input("Does an if statement need an else statement: ")
if (q.lower() == "no"):
  all["Computer Science"] += 1
  print("Correct")

q = input("What are the outer electrons in an atom called that are involved in reactions: ")
if ("valence" in q.lower()):
  all["Science"] += 1
  print("Correct")

q = input("What type of drug is alcohol: ")
if ("depressant" in q.lower()):
  all["Psychology"] += 1
  print("Correct")

q = input("What is a derivative: ")
if ("slope" in q.lower()):
  all["Math"] += 1
  print("Correct")

q = input("Name one English conjunction: ")
if (q.lower() == "for" or q.lower() == "and" or q.lower() == "nor" or q.lower() == "but" or q.lower() == "or" or q.lower() == "yet" or q.lower() == "so"):
  all["English"] += 1
  print("Correct")

q = input("Is Java object oriented: ")
if ("yes" in q.lower()):
  all["Computer Science"] += 1
  print("Correct")

print("\n\n")

lNum = max(all.values())
c=0
for major in all.keys():
  if (lNum>2 and all[major]==lNum):
    c+=1
    print("You should consider doing",major + ", your score was",str(lNum)+"! Enjoy")
string = "\n\n Only two majors appeared... Maybe consider a major and a minor?" if c==2 else "\n\nWoah, that's a lot! But I'm sure you have something in mind already of what you want to be :)"
if(c==len(all.values())):
  string = "\n\nThat's pretty well-rounded! I hope you have a plan for college because I don't have one for ya' XD"
elif(c==0):
  string = "\n\nYou're really bad at this! Maybe do nothing with yourself in the future because you're doing nothing with yourself now."
elif(c==1):
  string = "\n\nJust one major... looks like your goals are set :D" 
print(string,"\n\n")
print("If you are confused about what college to apply to, then take this short quiz:")
print("https://www.niche.com/about/college-quiz/")
