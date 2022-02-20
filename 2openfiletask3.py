def number_of_words():
    file_list = ['1.txt', '2.txt', '3.txt']
    sum_lines_list = []
    for k in file_list:
        sum_lines = 0
        with open(k, encoding='utf-8') as f:
            for file in f:
                sum_lines += 1
                sum_lines_list.append(sum_lines)
    file_zip = zip(file_list, sum_lines_list)
    file_zip_sorted = sorted(file_zip, key=lambda x: x[1])
    # print(file_zip_sorted)
    with open('result_file.txt', 'w', encoding='utf-8') as file:
        for k in file_zip_sorted:
            file.write(k[0] + '\n')
            file.write(str(k[1]) + '\n')
            with open(k[0], encoding='utf-8') as curr_file:
                for strings in curr_file:
                    file.write(strings)
            file.write('\n')
    return ('Результат в файле: result_file.txt')
print(number_of_words())
