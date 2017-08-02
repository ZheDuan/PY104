from sys import argv

script, first_name, last_name = argv
response = '> '

print(f"Hi {first_name} {last_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {first_name} {last_name}?")
likes = input(response)

print(f"Where do you live {first_name} {last_name}?")
lives = input(response)

print(f"What kind of computer do you have?")
computer = input(response)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
