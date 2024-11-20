import re

from bs4 import BeautifulSoup

from module.network import RequestContent
from module.utils import save_image


def nyaa_parser(homepage: str):
    return "", "第x季"


if __name__ == '__main__':
    homepage = "https://nyaa.si/view/1901784"
    print(nyaa_parser(homepage))
