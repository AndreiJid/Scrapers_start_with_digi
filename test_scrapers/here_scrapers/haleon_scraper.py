#
#
#
# New Company - Haleon
# Link to jobs - https://careers.haleon.com/en-gb/jobs?location=Romania&stretch=10&stretchUnit=MILES&page=1
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import requests
#
import uuid


def run_scraper() -> tuple:
    """
    Collect data with one requests,
    ... all from haleon.
    """

    response = requests.get('https://careers.haleon.com/api/jobs?page=1&location=Romania&stretch=10&stretchUnit=MILES&sortBy=relevance&descending=false&internal=false',
                           headers=DEFAULT_HEADERS).json()

    lst_with_data = []
    for dt in response['jobs']:
        slug_link = dt['data']['slug']
        title = dt['data']['title']
        location = dt['data']['country_code']

        # check country code!
        if location != 'RO':
            location = 'Multiple'

        lst_with_data.append({
                    "id": str(uuid.uuid4()),
                    "job_title": title,
                    "job_link":  f"https://careers.haleon.com/en-gb/jobs/{slug_link}?lang=en-us&previousLocale=en-US",
                    "company": "haleon",
                    "country": "Romania",
                    "city": location
                    })

    return lst_with_data, len(lst_with_data)
