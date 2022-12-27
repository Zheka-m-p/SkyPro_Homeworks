import json


def print_last5_operation(file_name):
    with open(file_name, encoding='utf-8') as f:
        all_data = json.load(f)
        all_data = sorted(all_data, key=lambda x: x['date'], reverse=True)
    count = 0

    def mask_the_data_payment(value):
        if 'Счет' in value:
            return f"Счет **{value[-4:]}"
        else:
            value = list(value)
            for i in range(-5, -11, -1):
                value[i] = '*'
            for i in (-5, -9, - 13):
                value[i] += ' '
            return ''.join(value)

    for payment in all_data:
        year, month, day = payment['date'].split('T')[0].split('-')
        date = '.'.join([day, month, year])  # тут не писал обработку, просто дату в двух местах добавил сам в json
        description = payment['description']
        from_ = mask_the_data_payment(payment.get('from', 'данные не известны'))  # для избежания key error 'from'
        to_ = mask_the_data_payment(payment['to'])
        amount = payment['operationAmount']['amount']
        currency = payment['operationAmount']['currency']['name']
        ans = f"{date} {description}\n" \
              f"{from_} -> {to_}\n" \
              f"{amount} {currency}\n"
        print(ans)

        count += 1
        if count == 5:
            break


if __name__ == '__main__':
    print_last5_operation('operations.json')
