from csv import reader

flag = 0

output = open('results.txt', 'w')
search = input('Search for: ')
with open('civic.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        lower_case = row[2].lower()
        index = lower_case.find(search.lower())
        if index != -1:
            print(row[2])
            flag = 1
            output.write(f'{row[0]}. {row[2]}. Цена {row[8]} рублей.\n')

    if flag == 0:
        print('Nothing found.')

output.close()