class TxtToFormatAdapter:
    """Adapter to convert from Txt format"""

    def __init__(self, file_path):
        self.file_path = file_path

    def convert_from_txt_to_html(self):
        """Adapter method to convert from txt to html format"""
        with open(self.file_path) as file:
            lines = file.readlines()
        tags = lines[0].replace('\n', '').split(',')
        value_data_txt = lines[1:]
        list_of_values = [item.replace('\n', '').split(',') for item in value_data_txt]
        html_result = ''
        for each_row in list_of_values:
            tag_value_dictionary = dict(zip(tags, each_row))
            for tag, value in tag_value_dictionary.items():
                html_result += f'<{tag}>{value}</{tag}>\n'
        return html_result


if __name__ == '__main__':
    html_formatted_result = TxtToFormatAdapter('13_1_txt_to_convert.txt').convert_from_txt_to_html()
    print(html_formatted_result)
