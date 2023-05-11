#
#
#
# New Scraper for upteam
# Link to this company ---> https://www.upteam.com/careers
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
#
from L_00_logo import update_logo
#
import requests
from bs4 import BeautifulSoup
#
import uuid


def collect_data_from_upteam() -> list:
    """
    This func() return all data from upteam.
    """

    response = requests.get(url='https://www.upteam.com/careers',
                            headers=DEFAULT_HEADERS
                            )
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_='w-dyn-item')

    lst_with_data = []
    for sd in soup_data:
        link = sd.find('a')['href']
        title = sd.find('h2').text

        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": 'https://www.upteam.com' + link,
            "company": "upteam",
            "country": "Romania",
            "city": "Romania"
            })

    return lst_with_data


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'upteam'
data_list = collect_data_from_upteam()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('upteam', 'https://global-uploads.webflow.com/6400e0ba2d1b077f024a81b0/6400edbf3cc188c78f15c3c1_UpTeam_logo.svg'))
