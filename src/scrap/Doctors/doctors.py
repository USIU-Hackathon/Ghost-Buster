from urllib2 import urlopen
from bs4 import BeautifulSoup


def get_data(url):
    """
    Function that takes url from medicaldoctors.co.ke and returns docotrs info
    :param url: link
    :return:list
    """

    doctors_list = []
    soup = BeautifulSoup(urlopen(url))
    table = soup.find('table')
    rows = table.find_all('tr')

    for row in rows:
        row_data = row.find_all('td')
        if len(row_data) == 0:
            pass
        else:
            # print '-----------------------'
            name = row_data[0].get_text().strip()
            reg_date = row_data[1].get_text().strip()
            reg_no = row_data[2].get_text().strip()
            address = row_data[3].get_text().strip()
            qualifications = row_data[4].get_text().strip()
            speciality = row_data[5].get_text().strip()
            sub_speciality = row_data[6].get_text().strip().strip('\n')
            doctors_list.append((name, reg_date, reg_no, address, qualifications, speciality, sub_speciality))

    return doctors_list

url = 'http://medicalboard.co.ke/online-services/retention/?currpage='
full_list = []
for i in range(1, 170):
    print(len(full_list))
    full_list += get_data(url+str(i))
    print(full_list)

