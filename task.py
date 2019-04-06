import cgi
import json
import re
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


def tag_converter(s):
    #converts string of type "tag.class1.class2#idx"
    #to <tag class="class1 class2" id="idx">
    tagpattern = "(^\w+)"
    classpattern = "\.(\w+\-*\w*)"
    idpattern = "\#(\w+\-*\w*)"

    tag = re.findall(tagpattern, s)
    classes = re.findall(classpattern, s)
    tag_id = re.findall(idpattern, s)

    classes_str = " ".join(c for c in classes)
    id_str = " ".join(i for i in tag_id)
    tag_stuff = ""
    if classes_str != "":
        tag_stuff += ' class="{0}"'.format(classes_str)
    if id_str != "":
        tag_stuff += ' id="{0}"'.format(id_str)

    return {"tag": tag[0], "attributes": tag_stuff}


def json_to_html_converter(json_list):
    html_str = ""
    if isinstance(json_list, list):
        for dic in json_list:
            html_block = ""
            for key, value in dic.items():
                if isinstance(value, list):
                    value = json_to_html_converter(value)
                elif isinstance(value, str):
                    value = cgi.escape(value)

                converted_tag = tag_converter(key)

                html_line = "<{key} {attributes}>{title}</{key}>".format(
                    key   = converted_tag['tag'],
                    attributes = converted_tag['attributes'],
                    title = value)
                html_block += html_line

            html_block = "<li>{li_block}</li>".format(
                li_block = html_block)
            html_str += html_block

        html_str = "<ul>{ul_block}</ul>".format(
            ul_block = html_str)

    else:
        for key, title in json_list.items():
            html_line = "<{key}>{title}</{key}>".format(
                key   = key,
                title = title)
            html_str += html_line

    return html_str


def main():
    js_text = read_input_json_file('test5.json')
    html_str = json_to_html_converter(js_text)
    write_str_to_html_file(html_str, OUTPUT_HTML_FOLDER + '/' + '5.html')

if __name__ == '__main__':
    main()
