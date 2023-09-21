Name = ['Joe','William','Harry','Elis','Jack']
Mood = ['happy','sad','angry','depressed','normal']
Action = ['smiling','crying','shouting','silent','coding']

def ReflexAgent(name,mood):
    action = ''
    if mood == 'happy':
        action = 'smiling'
    elif mood == 'sad':
        action = 'crying'
    elif mood == 'angry':
        action = 'shouting'
    elif mood == 'depressed':
        action = 'silent'
    elif mood == 'normal':
        action = 'coding'

    return action

name = input("Enter name: ")
mood = input("Enter mood: ")
if name in Name and mood in Mood:
    action = ReflexAgent(name,mood)
    print(name,"is",mood,"and is",action)
else:
    print("Invalid input")