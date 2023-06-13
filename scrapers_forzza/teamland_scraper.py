#
#
#
# Company -> teamland
# Link -> https://www.teamland.ro/index.php#joburi_table
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import requests
from bs4 import BeautifulSoup
#
import uuid


def get_data_from_teamland() -> list:
    """
    ... get data from API teamland.
    """

    response = requests.get(url='https://www.teamland.ro/j.php?_=1686681054574',
                            headers=DEFAULT_HEADERS).json()

    lst_with_data = []
    for dt in response['data']:
        link_id = dt[0]
        title = BeautifulSoup(dt[1], 'lxml').find('span').text
        location = BeautifulSoup(dt[2], 'lxml').find('span').text

        lst_with_data.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link":  f"https://www.teamland.ro/apply.php?id={link_id}#content",
                "company": "teamland",
                "country": "Romania",
                "city": location
                })

    return lst_with_data


# update data on peviitor!
@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'teamland'
data_list = get_data_from_teamland()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('teamland',
                  'https://www.teamland.ro/img/logo.png'
                  ))
