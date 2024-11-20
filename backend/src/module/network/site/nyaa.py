def rss_parser(soup):
    torrent_titles = []
    torrent_urls = []
    torrent_homepage = []
    for item in soup.findall("./channel/item"):
        torrent_titles.append(item.find("title").text)
        torrent_homepage.append(item.find("guid").text)
        torrent_urls.append(item.find("link").text)
    return torrent_titles, torrent_urls, torrent_homepage


def nyaa_title(soup):
    return soup.find("title").text
