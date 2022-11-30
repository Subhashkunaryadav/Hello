print ("Hello world")

message = "Hello world"
print (message)

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lace"
full_name = first_name + " " + last_name + "!"
print(full_name)

print ("python")
print ("\tpython")

print ("languages: \n\tpython \n\tC \n\tjava \n\tjavascript")

message  = "One of python's strengths is it's diverse community."
print (message)


responses = {}


polling_active = True

while polling_active:
    
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    
    responses[name] = response
    
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


