import getpass
import datetime

def main():
    name = getpass.getuser().capitalize()
    now = datetime.datetime.now()
    today = now.strftime('%d, %b %Y')
    time = now.strftime("%H:%M")

    print(f'Hello {name}!')
    print(f'Today is {today}.')
    print(f'It\'s {time} now.')

if __name__ == '__main__':
    main()
