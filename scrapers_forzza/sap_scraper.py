#
#
#
# Scrap data from SAP company
# link to this company -> https://jobs.sap.com/search/?q=&locationsearch=Romania&startrow=0&scrollToTable=True
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import requests
from bs4 import BeautifulSoup
#
import uuid


def return_soup(url: str):
    """
    This func() return soup object.
    """

    response = requests.get(
            url=url,
            headers=DEFAULT_HEADERS)

    return BeautifulSoup(response.text, 'lxml')


def get_jobs_num(url: str) -> int:
    """
    ... return jobs num from this company.
    """

    soup = return_soup(url=url)

    num = list(set([i.text for i in soup.find_all('span', class_='paginationLabel')]))

    return int(num[0].split()[-1])


def collect_data_from_sap() -> list:
    """
    Collect all data from this site.
    """

    # jobs num
    jobs_num = get_jobs_num(
            url='https://jobs.sap.com/search/?q=&locationsearch=Romania&startrow=0&scrollToTable=true')

    count = 0
    lst_with_data = []

    #
    while count < jobs_num:

        soup = return_soup(
                url=f'https://jobs.sap.com/search/?q=&locationsearch=Romania&startrow={count}&scrollToTable=true')

        soup_data = soup.find_all('span', class_='jobTitle hidden-phone')

        for sd in soup_data:
            link = sd.find('a')['href']
            title = sd.find('a').text

            lst_with_data.append({
                    "id": str(uuid.uuid4()),
                    "job_title": title,
                    "job_link":  'https://jobs.sap.com/' + link,
                    "company": "sap",
                    "country": "Romania",
                    "city": "Romania"
                    })

        count += 25

    # print jobs num
    print(f'Jobs on SAP == {len(lst_with_data)}')

    return lst_with_data


# update data on peviitor!
@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'sap'
data_list = collect_data_from_sap()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('sap',
                  'https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg/sap-logo-svg.svg'
                  ))
