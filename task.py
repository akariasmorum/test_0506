import json

TEST_CASES_FOLDER = 'test_cases'
OUTPUT_HTML_FOLDER = 'output_html'
def read_input_json_file(file_name):
    with open(TEST_CASES_FOLDER + '/' + file_name, 'r') as f:
        text = f.read()
        return json.loads(text)


def write_str_to_html_file(html_string, file_name):
    with open(file_name, 'w+') as f:
        f.write(html_string)

    return True


def json_to_html_converter(json_list):
    html_str = ""
    for dic in json_list:
        html_line = "<h1>{title}</h1><p>{body}</p>".format(
            title = dic.get('title'),
            body  = dic.get('body'))
        html_str += html_line
    return html_str


def main():
    js_text = read_input_json_file('test1.json')
    html_str = json_to_html_converter(js_text)
    write_str_to_html_file(html_str, OUTPUT_HTML_FOLDER + '/' + '1.html')

if __name__ == '__main__':
    main()
