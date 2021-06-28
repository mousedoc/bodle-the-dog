import os


def get_picture_string(path, reversed):
    file_list = sorted(os.listdir(path))

    if reversed:
        file_list.reverse()

    output = ''
    format = '![](./assets/{0})\n'
    for file_name in file_list:
        output += format.format(file_name)

    return output


def generate_readme(format_file_name, output_file_name, picture_string):
    output = None
    with open(format_file_name, 'r', encoding='utf8') as file:
        format = file.read()
        output = format.format(picture_string)

    with open(output_file_name, 'wt', encoding='utf8') as file:
        file.write(output)


if __name__ == "__main__":
    readme_output = get_picture_string('assets/', False)
    sorted_readme_output = get_picture_string('assets/', True)

    generate_readme('Format.txt', 'README.md', sorted_readme_output)
    generate_readme('SortedFormat.txt', 'SORTED-README.md',
                    readme_output)
