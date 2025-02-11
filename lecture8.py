"""Необходимо считать любой текстовый файл на вашем ПК (можно создать новый)
и создать на его основе новый файл, где содержимое будет записано в обратном порядке.
В конце программы вывести на экран оба файла - старый в неизменном виде и новый в обратном порядке.
"""

input_name = 'input.txt'
output_name = 'output.txt'

# Чтение содержимого исходного файла
with open(input_name, 'r', encoding='utf-8') as input_file:
    content = input_file.read()

# Запись содержимого в обратном порядке в новый файл
with open(output_name, 'w', encoding='utf-8') as output_file:
    output_file.write(content[::-1])

# Вывод содержимого обоих файлов на экран
print("Содержимое исходного файла:")
print(content)

print("\nСодержимое нового файла (в обратном порядке):")
with open(output_name, 'r', encoding='utf-8') as output_file:
    reversed_content = output_file.read()
    print(reversed_content)
