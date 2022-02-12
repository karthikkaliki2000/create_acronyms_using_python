#for example acronym of natural language proccessing is NLP
user_input = str(input("Enter a phrase:"))
acronym = ""
text = user_input.split()
for i in text:
    acronym += i[0].upper()
print(acronym)