from templates.text import TextTemplate


def process(input):
    help = '''Hey there! I'm the Dude! \n
Sample queries that work are:
Hi, dude!
Duuuuuude!
Yay!
How are you?
Do you know about God?
:P
:D
Goodbye dude!
help
Who are you?
Tell me a joke
Tell me a quote'''
    output = {
        'input': input,
        'output': TextTemplate(help).get_message(),
        'success': True
    }
    return output
