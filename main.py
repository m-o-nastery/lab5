import re
import csv

def task_1(title):
    with open(title, encoding='utf-8') as file, open('task_1.txt', 'w', encoding='utf-8') as task_1_output:
        text = file.read()
        pattern_1 = r"\b([A-Za-z]+(?:[-\'][A-Za-z]+)*)\s*,"
        pattern_2 = r'\[(.*?)\]'
        match_1 = re.findall(pattern_1, text)
        match_2 = re.findall(pattern_2, text)
        task_1_output.write('Все слова, после которых стоит запятая:\n')
        for row in range(len(match_1)):
            task_1_output.write(f'{row+1}. {match_1[row]}\n')
        task_1_output.write('-'*36)
        task_1_output.write('\nВся информация в квадратных скобках:\n')
        for row in range(len(match_2)):
            task_1_output.write(f'{row+1}. {match_2[row]}\n')
        # print(match_1)
        # print(match_2)


def task_2(title):
    with open(title, encoding='utf-8') as file, open('task_2.txt', 'w', encoding='utf-8') as task_2_output:
        text = file.read()
        pattern = r'(?<![\w/])#[0-9a-fA-F]{3,6}\b'
        match = re.findall(pattern, text)
        task_2_output.write('Все обозначения цветов:\n')
        for row in range(len(match)):
            task_2_output.write(f'{row+1}. {match[row]}\n')
        # print(match)
        

def task_3(title):
    with open(title, encoding='utf-8') as file, open('task_3.csv', 'w', newline='', encoding='utf-8') as task_3_output:
        text = file.read()

        pattern_1 = r'[\w]+@[\w.-]+\.[A-za-z]+'
        email = re.findall(pattern_1, text)

        pattern_2 = r'(?<=[\s])[A-Z][a-z]+'
        name = re.findall(pattern_2, text)

        pattern_3 = r'[\d]{4}-[\d]{2}-[\d]{2}'
        date = re.findall(pattern_3, text)

        pattern_4 = r'https?://[\w.\-/]*'
        website = re.findall(pattern_4, text)

        pattern_5 = r'(?<=[\s])([\d]+)\s'
        id = re.findall(pattern_5, text)

        rows = [[id[i], name[i], email[i], date[i], website[i]] for i in range(len(id))]
        
        writer = csv.writer(task_3_output, delimiter=';')
        writer.writerow(['ID', 'Name', 'Email', 'Date', 'Website'])
        writer.writerows(rows)


if __name__ == '__main__':
    task_1('task1-en.txt')
    task_2('task2.html')
    task_3('task3.txt')