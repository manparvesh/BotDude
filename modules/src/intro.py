from templates.text import TextTemplate

x = "Let me explain something to you. I'm the Dude. "
x += "So that's what you call me. You know, that"
x += " or, uh, His Dudeness, or uh, Duder, or El Duderino"
x += " if you're not into the whole brevity thing"


def process(input):
    output = {
        'input': input,
        'output': TextTemplate(x).get_message(),
        'success': True
    }
    return output
