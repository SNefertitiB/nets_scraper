import scraper_utils

def get_player_headers(sample_player:str):
    sample_player_soup = get_soup(sample_player)
    player_table = sample_player_soup.find('div', {'class': 'stats_pullout'})   # bs4.element.Tag

    p1 = player_table.find('div', {'class': 'p1'})
    p2 = player_table.find('div', {'class': 'p2'})

    headers_1_span = p1.find_all('span', {'class':'poptip'})             # bs4.element.ResultSet
    headers_2_span = p2.find_all('span', {'class':'poptip'})

    # Get the data-tip attribute from each span
    headers_1 = [span['data-tip'] for span in headers_1_span]
    headers_2 = [span['data-tip'] for span in headers_2_span]

    header = headers_1 + headers_2
    return header    # TODO: ideally clean up that last header

def zip_players_links(players_page:str) -> zip:
    player_list_soup = get_soup(players_page)
    players = []
    urls = []

    player_ul = player_list_soup.find('ul', {'class':'page_index'})
    letters_list = player_ul.find_all('li')
    for letter in letters_list:
        if letter.div != None:
            div = letter.div.find_all('a')
            players += [a.text for a in div]
            urls += [a['href'] for a in div]

    return zip(players, urls)


if __name__ == '__main__':
    sample_player_page = "https://www.basketball-reference.com/players/a/aldrila01.html"
    player_headers = get_player_headers(sample_player_page)

    player_list_page = 'https://www.basketball-reference.com/players/'
    players_urls = zip_players_links(player_list_page)

