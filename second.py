file_names = ['1.txt', '2.txt', '3.txt']
files_data = []


for file_name in file_names:
    with open(f'sorted/{file_name}', 'r') as file:
        lines = file.readlines()
        file_data = {
            'name': file_name,
            'line_count': len(lines),
            'content': lines
        }
        files_data.append(file_data)


sorted_files = sorted(files_data, key=lambda x: x['line_count'])

output_file = 'output.txt'

with open(output_file, 'w') as output:
    for file_data in sorted_files:
        output.write(file_data['name'] + '\n')
        output.write(str(file_data['line_count']) + '\n')
        output.writelines(file_data['content'])