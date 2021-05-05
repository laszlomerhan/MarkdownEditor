def menu():
    formatter = ['plain', 'bold', 'italic', 'link', 'inline-code', 'header', 'ordered-list', 'unordered-list', 'line-break']
    text = ''
    while True:
        user = input('- Choose a formatter: ')
        if user == '!help':
            print('''Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break
Special commands: !help !done''')
        elif user in formatter:
            if user == 'plain':
                text += f_plain()
            elif user == 'bold':
                text += f_bold()
            elif user == 'italic':
                text += f_italic()
            elif user == 'link':
                text += f_link()
            elif user == 'inline-code':
                text += f_inline_code()
            elif user == 'header':
                text += f_header()
            elif user == 'line-break':
                text += f_line_break()
            elif user == 'ordered-list':
                text +=
            print(text)
        elif user == '!done':
            break
        else:
            print('Unknown formatting type or command. Please try again')


def f_plain():
    return input('- Text: ')


def f_bold():
    return f"**{input('- Text: ')}**"


def f_italic():
    return f"*{input('- Text: ')}*"


def f_link():
    label = input('- Label: ')
    url = input('- URL: ')
    return f'[{label}]({url})'


def f_inline_code():
    return f"`{input('- Text: ')}`"


def f_header():
    level = int(input('- Level: '))
    if level not in range(1, 6):
        print('The level should be within the range of 1 to 6')
        return f_header()
    else:
        return f"{'#' * level} {input('- Text: ')}\n"


def ordered_list():


def unordered_list():
    


def f_line_break():
    return '\n'


menu()
