"""
Test for HTML Table requirements - minimum 10 rows with 4 `th` and 4 `tds`
"""
from file_clerk import clerk
import pytest
from webcode_tk import html_tools as html

required_table_elements = [("table", 1),
                           ("tr", 10),
                           ("th", 4),
                           ("td", 30)
                           ]


@pytest.fixture
def files():
    files = clerk.get_all_files_of_type("project/", "html")
    return files


@pytest.mark.parametrize("element,num", required_table_elements)
def test_files_for_table_elements(element, num, files):
    if not files:
        assert False
    for file in files:
        actual = html.get_num_elements_in_file(element, file)
        assert actual >= num
