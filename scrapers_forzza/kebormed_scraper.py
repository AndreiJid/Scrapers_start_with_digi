#
#
#
# Company -> kebormed
# Link -> https://kebormed.com/careers/index.html
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import requests
from bs4 import BeautifulSoup
#
import uuid


def get_data_from_site() -> list:
    """
    ... Return data with one requests.
    """

    response = requests.get(url='https://kebormed.com/careers/index.html',
                            headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('a')

    lst_with_data = []
    for dt in soup_data:
        if 'kebormed.com/careers' in dt['href']:
            link = dt['href']
            title = dt.find('div', class_='text').text.strip()
            location = dt.find('div', class_='location').text.strip()

            if 'Remote' in location:
                lst_with_data.append({
                    "id": str(uuid.uuid4()),
                    "job_title": title,
                    "job_link": link,
                    "company": "kebormed",
                    "country": "Romania",
                    "city": location
                    })

    return lst_with_data


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'kebormed'
data_list = get_data_from_site()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('kebormed',
                  'https://kebormed.com/images/logo.svg
                  ))
