"""
Test for HTML requirements
"""
from file_clerk import clerk
import pytest
from webcode_tk import html_tools as html

required_image_elements = [("figure", 2),
                           ("img", 2),
                           ("figcaption", 2)
                           ]


@pytest.fixture
def files():
    files = clerk.get_all_files_of_type("project/", "html")
    return files


@pytest.mark.parametrize("element,num", required_image_elements)
def test_files_for_required_elements(element, num, files):
    if not files:
        assert False
    for file in files:
        actual = html.get_num_elements_in_file(element, file)
        assert actual >= num
