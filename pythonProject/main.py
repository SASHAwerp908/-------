import requests

global get_ip
get_ip = input('[+] IP:')

def info():
    response = requests.get( f'http://ipinfo.io/{ get_ip }/json' )

    user_city = response.json()['city']

    global all_info
    all_info = f'\n<Информация>\n Сити : { user_city }\n'# вся инфа

    print(all_info)

def record():
    user_record = input('\n[?] Хотите получить информацию в текстовом документе? (д/н): ')

    if user_record == 'д':
        file = open('ip_data.txt', 'a')
        file.write(f'{ all_info }\n')
        file.close()

        print('\nВся информация находится в текстовом документе!"')

    if user_record == 'n':
        print('\n<O.K>')

def main():
    info()
    record()

main()