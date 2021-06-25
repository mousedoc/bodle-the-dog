import os


def get_picture_string(path):
    file_list = os.listdir(path)
    picture_string = '\n'.join(file_list)
    file_list.reverse()
    reversed_picture_string = '\n'.join(file_list)
    return {picture_string, reversed_picture_string}


def generate_readme(format_file_name, output_file_name, picture_string):
    output = None
    with open(format_file_name, 'r', encoding='utf8') as file:
        format = file.read()
        output = format.format(picture_string)

    print(f'--- {output_file_name} --- \n{output}\n\n\n')

    with open(output_file_name, 'wt', encoding='utf8') as file:
        file.write(output)


if __name__ == "__main__":
    picture_string, reversed_picture_string = get_picture_string('assets/')
    generate_readme('Format.txt', 'README.md', picture_string)
    generate_readme('SortedFormat.txt', 'SORTED-README.md',
                    reversed_picture_string)
