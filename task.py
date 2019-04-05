import json
from collections import OrderedDict

TEST_CASES_FOLDER = 'test_cases'
OUTPUT_HTML_FOLDER = 'output_html'
def read_input_json_file(file_name):
    with open(TEST_CASES_FOLDER + '/' + file_name, 'r') as f:
        text = f.read()
        return json.loads(text, object_pairs_hook = OrderedDict)


def write_str_to_html_file(html_string, file_name):
    with open(file_name, 'w+') as f:
        f.write(html_string)

    return True


def json_to_html_converter(json_list):
    html_str = ""
    if isinstance(json_list, list):
        for dic in json_list:
            html_block = ""
            for key, title in dic.items():
                html_line = "<{key}>{title}</{key}>".format(
                    key   = key,
                    title = title)
                html_block += html_line

            html_block = "<li>{li_block}</li>".format(
                li_block = html_block)
            html_str += html_block

        html_str = "<ul>{ul_block}</ul>".format(
            ul_block = html_str)

    else:
        raise  Exception('nothing to do here')        

    return html_str


def main():
    js_text = read_input_json_file('test3.json')
    html_str = json_to_html_converter(js_text)
    write_str_to_html_file(html_str, OUTPUT_HTML_FOLDER + '/' + '3.html')

if __name__ == '__main__':
    main()
