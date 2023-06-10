#
#
#
# Scrape new company -> Azets
# Link to this site ---> https://www.azets.ro/talentlink/
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import requests
from bs4 import BeautifulSoup
#
import uuid


def run_scraper() -> tuple:
    """
    Colect data from sites.
    """

    session = requests.Session()
    response = session.get(url='https://www.azets.ro/talentlink/',
                           headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_='talentlink-expandable-item mb-2')

    lst_with_data = []
    for sd in soup_data:
        link = sd.find('div', class_='job-title-value pb-3').find('a')['href']
        title = sd.find('div', class_='job-title-value pb-3').find('a').text

        lst_with_data.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": "https://www.azets.ro" + link,
                "company": "azets",
                "country": "Romania",
                "city": "Romania"
            })

    return lst_with_data, len(lst_with_data)
