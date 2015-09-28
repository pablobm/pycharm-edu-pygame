from test_helper import run_common_tests, failed, passed, get_answer_placeholders
import re

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    number = re.compile('^[0-9]+$')

    width = placeholders[0]
    if number.match(width):
        passed()
    else:
        failed("The width should be a number")

    height = placeholders[1]
    if number.match(height):
        passed()
    else:
        failed("The height should be a number")

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()