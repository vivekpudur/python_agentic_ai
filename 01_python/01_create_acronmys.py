#### Create Acronyms using Python
user_input = input("Enter a phrase to create an acronym: ")  ## Input from user
text = user_input.split() ## split the phrase into words
acronym = "" ## Initialize an empty string to store the acronym
for word in text: ## Loop through each word in the list
    acronym = acronym + word[0].upper() ## Take the first letter of each word, convert to uppercase, and add to acronym
print("The acronym is:", acronym)   ## Print the final acronym