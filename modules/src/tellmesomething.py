from templates.text import TextTemplate


def process(input):
    tellmesomething = '''What do you want to know? 
Sample queries that work are:
Hi, dude!
Duuuuuude!
Yay!
How are you?
What are you doing?
Do you know about God?
Who made you?
Who is Man Parvesh?
:P
:D
Goodbye dude!
help
Who are you?
Tell me a joke
Tell me a quote'''
    output = {
        'input': input,
        'output': TextTemplate(tellmesomething).get_message(),
        'success': True
    }
    return output
