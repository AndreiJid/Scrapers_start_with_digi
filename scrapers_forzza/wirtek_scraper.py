#
#
#
# Scrape data from wirtek.com/compile
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
#
import requests
from bs4 import BeautifulSoup
#
import uuid


def data_scrape_from_wirtek():
    """
    This func() is about scrape wirtek.
    """

    response = requests.get('https://www.wirtek.com/careers', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    job_grid = soup.find_all('div', class_='careers-grid__job')

    lst_with_jobs_data = []
    for job in job_grid:
        link_job = job.a['href']
        title_job = job.find('div', class_='careers-grid__job-name').text.strip()

        lst_with_jobs_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title_job,
            "job_link":  link_job,
            "company": "wirtek",
            "country": "Romania",
            "city": "Romania"
            })

    return lst_with_jobs_data


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'wirtek'
data_list = data_scrape_from_wirtek()
scrape_and_update_peviitor(company_name, data_list)
