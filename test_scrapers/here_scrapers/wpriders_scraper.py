#
#
#
# Company - wpriders
# Link - https://wpriders.com/careers/
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import requests
from bs4 import BeautifulSoup
#
import uuid


def run_scraper() -> list:
    '''
    ... get all data from site
    with one requests.
    '''

    response = requests.get(url='https://wpriders.com/careers/',
                            headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_="elementor-widget-wrap")

    lst_with_data = []
    for dt in soup_data:
        #
        link = None
        title = None
        #
        link = dt.find('a', class_='btn_secondary')
        title = dt.find('h2', class_='elementor-heading-title elementor-size-default')
        if title and title.find('a'):
            pass
        else:
            if title is not None:
                if 'apply now' not in title.text.lower():
                    lst_with_data.append({
                        "id": str(uuid.uuid4()),
                        "job_title": title.text.strip(),
                        "job_link":  link['href'],
                        "company": "wpriders",
                        "country": "Romania",
                        "city": "Remote"
                        })

    # dict with no duplicate
    new_list_with_data = []

    # remove duplicates
    removed_links = []
    for saga in lst_with_data:
        for key, value in saga.items():
            if key == 'job_link' and value not in removed_links:
                new_list_with_data.append(saga)

                removed_links.append(value)

    return new_list_with_data, len(new_list_with_data)
