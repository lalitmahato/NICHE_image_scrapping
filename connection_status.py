import requests
from helper import generate_url
from scrapping import extractInfo, get_institute_name
import time
from db_configuration import db
from check_database import check_availability


# Function that checks connection status and proceed for extracting data
def Connection_Status(url, name_institute, num, id):
    try:
        records = ['College_Details', 'Graduate_Schools', 'K_12']
        url_list = ['https://www.niche.com/colleges/', 'https://www.niche.com/graduate-schools/', 'https://www.niche.com/k12/']
        page = requests.get(url,timeout=100, headers={'User-Agent': 'Mozilla/5.0'})
        # If server responce without error the if block will execute
        if page.status_code == requests.codes.ok :
            # print connection status
            print("Connection Status Code: ", page.status_code)
            print("Information Retereaved:", page.status_code == requests.codes.ok)
            extractInfo(page, records[num], name_institute, id)
            return True
        # If server responce bad data or does not response or some error occure belows block will execute
        # Handel connection status code
        elif page.status_code == 404:
            # print connection status
            print("Connection Status Code: ", page.status_code)
            print("Information Reterived:", page.status_code == requests.codes.ok)
            print("Unable to reterive trying for others levels \n\n")
            # need to try for other levels
            num = num + 1
            if num < 3 :
                new_url = generate_url(url_list[num], name_institute, '-')
                Connection_Status(new_url, name_institute, num, id)
            else:
                error_to_scrap = {
                    'id': int(id),
                    'url': url,
                    'name_of_institute': name_institute,
                    'connection_status_code': page.status_code,
                    'information_retereaved': page.status_code == requests.codes.ok
                }
                # print connection status
                print("Unable to scrap data\n")
                print("Connection Status: \n", error_to_scrap)
                print("Adding to the database....")
                db['status'].insert_one(error_to_scrap) # adding to the database
                print("Successfully added to the database....")
                return False

        elif page.status_code == 403:
            # print connection status
            print("Connection Status Code: ", page.status_code)
            print("Information Retereaved:", page.status_code == requests.codes.ok)
            print("waiting for some minutes.....")
            time.sleep(300) # make the program wait for some time
            print("Trying to retreave data again!...\n\n")
            Connection_Status(url, name_institute, num, id) # Try to retreave data again
        else:
            error_to_scrap = {
                'id': int(id),
                'url': url,
                'name_of_institute': name_institute,
                'connection_status_code': page.status_code,
                'information_retereaved': page.status_code == requests.codes.ok
            }
            # print connection status
            print("Unable to scrap data\n")
            print("Connection Status: \n", error_to_scrap)
            print("Adding to the database....")
            db['status'].insert_one(error_to_scrap) # adding to the database
            print("Successfully added to the database....")
            return False
    except:
        error_to_scrap = {
            'id': int(id),
            'url': url,
            'name_of_institute': name_institute,
            'connection_status_code': page.status_code,
            'information_retereaved': page.status_code == requests.codes.ok
        }
        # print connection status
        print("Unable to scrap data\n")
        print("Connection Status: \n", error_to_scrap)
        print("Adding to the database....")
        db['status'].insert_one(error_to_scrap) # adding to the database
        print("Successfully added to the database....")
        return False

