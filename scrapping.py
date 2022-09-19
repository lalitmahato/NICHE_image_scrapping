from bs4 import BeautifulSoup
from helper import Remove_Character, Get_Position_Value, Join_Value_With, Remove_Unusal_Spaces, Name_Attribute
from db_configuration import db
import re
from helper import *


#Function to Scrap Data
def extractInfo(HtmlPage, collection_name, name_institute, id):
    soup = BeautifulSoup(HtmlPage.content,'html.parser')
    # print(soup)
    image_div = soup.find('div', class_='postcard__figure__image')
    image_text = str(image_div.style.text)
    # print(image_text, type(image_text))
    splited_url = image_text.rstrip().split()
    # print(splited_url)
    url_lists = []
    for i in splited_url:
        if i.startswith('url'):
            url_lists.append(i.rstrip())
    small_image = str(url_lists[0])[4:-2]
    big_image = str(url_lists[2])[4:-2]
    print(small_image)
    print(big_image)

    # Adding to the database
    db['images'].insert_one({
        'uid': int(id),
        'institute_name': name_institute,
        'institutation_type': collection_name,
        'small_image':small_image,
        'big_image': big_image,
    })
    db['status'].insert_one({
        'uid': int(id),
        'institute_name': name_institute,
        'institutation_type': collection_name,
        'scrap_status': True
    }) # adding scrapped status
    print("Successfully added to the database !!!\n")
    # # Header block
    # header_block = soup.find('div', class_="postcard__content postcard__content--primary")
    # # print(header_block)
    # Institute_Data["Institute_Name"] = Remove_Unusal_Spaces(header_block.find('h1', class_= "postcard__title"))
    # try:
    #     Institute_Data["Position"] = int(Get_Position_Value(header_block.find('div', class_="postcard__badge"), 1))
    # except:
    #     Institute_Data["Position"] = Get_Position_Value(header_block.find('div', class_="postcard__badge"), 1)

    # try:
    #     Institute_Data["Rating"] = float(Get_Position_Value(header_block.find('span', class_="visually-hidden"), 1))
    # except:
    #     Institute_Data["Rating"] = Get_Position_Value(header_block.find('span', class_="visually-hidden"), 1)
    # try:
    #     Institute_Data["Reviews"] = int(Get_Position_Value(header_block.find('span', class_= "review__stars__number__reviews"), 0))
    # except:
    #     Institute_Data["Reviews"] = Get_Position_Value(header_block.find('span', class_= "review__stars__number__reviews"), 0)

    # # print(Institute_Data)


    # # Report Card
    # Report_Card = {}
    # try:
    #     report_card = soup.find(id= "report-card")
    #     overall_grade = report_card.find('div', class_="overall-grade__niche-grade")
    #     individual_grade = report_card.find_all('ol', class_="ordered__list__bucket")

    #     grade = overall_grade.find_all('div', class_="niche__grade")
    #     for i in grade:
    #         Report_Card["Overall_Grade"] = Get_Position_Value(i, 1)

    #     Individual_Grade = {}
    #     for ig in individual_grade:
    #         list_grade = ig.find_all('li')
    #         for i in list_grade:
    #             Subject = Name_Attribute(i.div.div)
    #             grade = i.find_all('div', class_="niche__grade")
    #             for j in grade:
    #                 grade = j.get_text(separator=' ').rstrip().split()
    #                 grade = ' '.join(grade[1:])
    #             Individual_Grade[Subject] = grade
    #     Report_Card["Individual_Grade"] = Individual_Grade
    #     Institute_Data['Report_Card'] = Report_Card
    #     # print(Report_Card)
    # except:
    #     pass


    # # About
    # try:
    #     About = {}
    #     info = soup.find('span', class_="bare-value")
    #     About["About"] = Join_Value_With(info, ' ')

    #     URL_Info = soup.find_all('a', class_="profile__website__link")
    #     for url_i in URL_Info:
    #         About["URL"] = url_i.get_text()
    #     Address = soup.find_all('address', class_= "profile__address--compact")
    #     for address in Address:
    #         About["Address"] = Join_Value_With(address, ' ')

    #     search_tag_label = soup.find_all('div', class_= "search-tags__label")
    #     for i in search_tag_label:
    #         search_tag_label = Join_Value_With(i, ' ')
    #     # print(search_tag_label)
    #     search_tag = soup.find_all('li', class_="search-tags__wrap__list__tag")
    #     Tag = []
    #     # for i in search_tag_label:
    #     for i in search_tag:
    #         tag = Join_Value_With(i.a, ' ')
    #         Tag.append(tag)
    #     About["Search_Tags"] = {"Label": search_tag_label, 'Tags':Tag}
    #     # print(About)
    #     Institute_Data['About'] = About
    # except:
    #     pass


    # # Rankings
    # try:
    #     Rankings = []
    #     rank = soup.find_all('li', class_="rankings__collection__item")
    #     for ra in rank:
    #         rank_data = {}
    #         Rank_Data = ra.get_text(separator=' ').rstrip().split()
    #         Rank_Title = ' '.join(Rank_Data[:-3])
    #         Rank = int(''.join(Rank_Data[-3].split(",")))
    #         Rank_In = int(''.join(Rank_Data[-1].split(",")))

    #         rank_data['Rank_Title'] = Rank_Title
    #         rank_data['Rank'] = Rank
    #         rank_data['Rank_In'] = Rank_In
    #         Rankings.append(rank_data)
    #     # print(Rankings)
    #     Institute_Data['Rankings'] = Rankings
    # except:
    #     pass


    # # Admissions
    # try:
    #     Admissions = {}
    #     admi = soup.find( id="admissions")
    #     admi_label = Remove_Unusal_Spaces(admi.find('div', class_="scalar__label"))
    #     admi_value = Remove_Unusal_Spaces(admi.find('div', class_="scalar__value"))
    #     Admissions[admi_label] = admi_value

    #     admi_l_v = admi.find_all("div", class_="scalar--three")
    #     for l_v in admi_l_v:
    #         label = Remove_Unusal_Spaces(l_v.find('div', class_="scalar__label"))
    #         value = l_v.find('div', class_="scalar__value")
    #         if value == None:
    #             value = '-'
    #         else:
    #             value = Remove_Unusal_Spaces(value)
    #         Admissions[label] = value

    #     Also_Apply = []
    #     also_apply = admi.find_all('li', class_="popular-entities-list-item")
    #     for j in also_apply:
    #         Grade = Get_Position_Value(j.div.div.div , -1)
    #         Name_Of_Insititute = Remove_Unusal_Spaces(j.find('div', class_="popular-entity__name" ))
    #         Also_Apply.append({"Grade": Grade, "Name_Of_Insititute": Name_Of_Insititute})

    #     Admissions["Students_Also_Apply"] = Also_Apply
    #     # print(Admissions)
    #     Institute_Data['Admissions'] = Admissions
    # except:
    #     pass


    # # Cost
    # try:
    #     Cost = {}
    #     cost = soup.find( id="cost")
    #     c_lab = []
    #     c_val = []
    #     cost_label = cost.find_all('div', class_="scalar__label")
    #     cost_value = cost.find_all('div', class_="scalar__value")
    #     national_value = cost.find('div' , class_="scalar__national__value")

    #     for cl in cost_label:
    #         c_lab.append(Name_Attribute(cl.span))
    #     for cv in cost_value:
    #         try:
    #             c_val.append(int(Remove_Character(cv.span, '$,')))
    #         except:
    #             c_val.append(Remove_Character(cv.span, '$,'))

    #     for i in range(len(c_lab)):
    #         Cost[c_lab[i]] = c_val[i]
    #     Cost[Get_Position_Value(national_value,0)] = Get_Position_Value(national_value,1)
    #     # print(Cost)
    #     Institute_Data['Cost'] = Cost
    # except:
    #     pass


    # # Majors
    # try:
    #     Majors = []
    #     majors = soup.find( id="majors")
    #     majors_sub = majors.find_all('li', class_="popular-entities-list-item")
    #     for maj_sub in majors_sub:
    #         Subject = maj_sub.find('div', class_="popular-entity__name")
    #         Subject = Name_Attribute(Subject)
    #         Graduates = maj_sub.find('div', class_="popular-entity-descriptor")
    #         Graduates = int(Get_Position_Value(Graduates, 0))
    #         Majors.append({'Subject': Subject, 'Graduates': Graduates})
    #     # print(Majors)
    #     Institute_Data['Majors'] = Majors
    # except:
    #     pass


    # # Students
    # try:
    #     Students = {}
    #     students = soup.find( id="students")
    #     # print(students)
    #     stud_label = Remove_Unusal_Spaces(students.find('div', class_="scalar__label"))
    #     stud_value = Remove_Unusal_Spaces(students.find('div', class_="scalar__value"))
    #     # print(stud_label, stud_value)
    #     Students[stud_label] = stud_value
    #     stud_l_v = admi.find_all("div", class_="scalar--three")
    #     for l_v in stud_l_v:
    #         stud_label = Remove_Unusal_Spaces(l_v.find('div', class_="scalar__label"))
    #         stud_value = l_v.find('div', class_="scalar__value")
    #         if stud_value == None:
    #             stud_value = '-'
    #         else:
    #             stud_value = Remove_Unusal_Spaces(stud_value)
    #         Students[stud_label] = stud_value

    #     Poll = {}
    #     Report = []
    #     Poll_Question =  Remove_Unusal_Spaces(students.find('div', class_="poll__table__body"))
    #     Responses = students.find('div', class_="poll__table__count")
    #     if Responses == None:
    #         Responses = 0
    #     else:
    #         Responses = Get_Position_Value(Responses, -2)
    #         report = students.find_all('li', class_="poll__table__result__item")
    #         for r in report:
    #             result_label = Name_Attribute(r.find('div', class_="poll__table__result__label"))
    #             result_percent = Remove_Unusal_Spaces(r.find('div', class_="poll__table__result__percent"))
    #             Report.append({'Option': result_label, 'Percent': result_percent})
    #         Poll['Poll_Question'] = Poll_Question
    #         Poll['Responses'] = Responses
    #         Poll['Report'] = Report
    #         Students['Poll'] = Poll
    #     # print(Students)
    #     Institute_Data['Students'] = Students
    # except:
    #     pass


    # # Campus Life
    # try:
    #     Campus_Life = {}
    #     campus_life = soup.find(id= 'campus-life')
    #     if campus_life == None:
    #         pass
    #     else:
    #         Live_On_Campus_lab = Name_Attribute(campus_life.find('div', class_="scalar__label"))
    #         Live_On_Campus_val = Remove_Unusal_Spaces(campus_life.find('div', class_="scalar__value"))
    #         Campus_Life[Live_On_Campus_lab] = Live_On_Campus_val

    #         Campus_Life_Poll = []
    #         campus_life_poll = campus_life.find_all('div', class_="poll__single__value")
    #         for clp in campus_life_poll:
    #             p = clp.span.get_text(separator=' ').rstrip().split()
    #             Poll_Label = ' '.join(p[:-2])
    #             Poll_Responses = p[-2]
    #             Poll_Value = Get_Position_Value(clp.div, 0)
    #             Campus_Life_Poll.append({'Poll_Value': Poll_Value, 'Poll_Label':Poll_Label, 'Poll_Responses':Poll_Responses})

    #         cl_poll = []
    #         Campus_Life_Poll_Question =  Remove_Unusal_Spaces(campus_life.find('div', class_="poll__table__body"))
    #         Campus_Life_Responses = int(Get_Position_Value(campus_life.find('div', class_="poll__table__count"), -2))
    #         campus_life_report = campus_life.find_all('li', class_="poll__table__result__item")
    #         for clr in campus_life_report:
    #             result_label = Name_Attribute(clr.find('div', class_="poll__table__result__label"))
    #             result_percent = Remove_Unusal_Spaces(clr.find('div', class_="poll__table__result__percent"))
    #             cl_poll.append({'Option': result_label, 'Percent': result_percent})
    #         Campus_Life_Poll.append({'Poll_Question': Campus_Life_Poll_Question, 'Responses': Campus_Life_Responses, 'Report': cl_poll})

    #         Campus_Life["Poll"] = Campus_Life_Poll
    #     # print(Campus_Life)
    #     Institute_Data['Campus_Life'] = Campus_Life
    # except:
    #     pass


    # # After College
    # try:
    #     After_College = {}
    #     After_Col = []
    #     after_college = soup.find(id='after')
    #     AC_Label = []
    #     AC_Value = []
    #     AC_National = []

    #     ac_label = after_college.find_all('div', class_="scalar__label")
    #     ac_value = after_college.find_all('div', class_="scalar__value")
    #     ac_national = after_college.find_all('div', class_="scalar__national__value")

    #     for acl in ac_label:
    #         AC_Label.append(Name_Attribute(acl.span))
    #     for acv in ac_value:
    #         try:
    #             AC_Value.append(int(Remove_Character(acv.span, "$,")))
    #         except:
    #             AC_Value.append(Remove_Character(acv.span, "$,"))
    #     for acn in ac_national:
    #         AC_National.append(Get_Position_Value(acn, -1))
    #     for i in range(len(AC_Label)):
    #         After_Col.append({"Label":AC_Label[i], "Value":AC_Value[i], "National":AC_National[i]})
    #     After_College["After_College"] = After_Col

    #     after_college_poll = after_college.find_all('div', class_="poll__single__value")
    #     for acp in after_college_poll:
    #         p = acp.span.get_text(separator=' ').rstrip().split()
    #         Poll_Label = ' '.join(p[:-2])
    #         Poll_Responses = p[-2]
    #         Poll_Value = Get_Position_Value(acp.div, 0)
    #         After_College["Poll"] = {'Poll_Value': Poll_Value, 'Poll_Label':Poll_Label, 'Poll_Responses':Poll_Responses}
    #     # print(After_College)
    #     Institute_Data['After_College'] = After_College
    # except:
    #     pass


    # # Similar Colleges
    # try:
    #     Similar_Colleges = []
    #     similar_colleges = soup.find(id='similar-colleges')
    #     for sc in similar_colleges.find_all('li', class_="similar-entity"):
    #         Grade = Get_Position_Value(sc.div.div, -1)
    #         Name_Of_Ins = Remove_Unusal_Spaces(sc.find('a', class_="chip__name"))
    #         d = sc.find('div', class_="review__stars").get_text(separator=' ').rstrip().split()
    #         Rating = d[1]
    #         Reviews = d[-2]
    #         Similar_Colleges.append({"Name_Of_Insititute": Name_Of_Ins, "Grade": Grade, "Rating":Rating, "Reviews":Reviews})
    #     # print(Similar_Colleges)
    #     Institute_Data['Similar_Colleges'] = Similar_Colleges
    # except:
    #     pass


    # # Reviews
    # try:
    #     Reviews = []
    #     reviews = soup.find(id='reviews')
    #     review_rating = reviews.find_all('li', class_="review__chart__item review__chart__item")
    #     for rr in review_rating:
    #         Rate = int(Get_Position_Value(rr.find('span', class_="visually-hidden"), 1))
    #         Level = Get_Position_Value(rr.find('div', class_="review__chart__item__label"), -1)
    #         Review_Count = int(Get_Position_Value(rr.find('div', class_="review__chart__item__total"), 0))
    #         Reviews.append({"Rate": Rate, "Level": Level, "Reviews": Review_Count})
    #     Institute_Data["Reviews"] = Reviews
    # except:
    #     pass

    # # print(Institute_Data)

    # # Adding to the database
    # db[collection_name].insert_one(Institute_Data) # adding scrapped data into database
    # filter = {'id': id}
    # new_value = {"$set":{'scrap_status': True}}
    # db['status'].update_one(filter, new_value) # adding scrapped status
    # print("Successfully added to the database !!!\n")


def get_institute_name(page):
    soup = BeautifulSoup(page.content,'html.parser')
    header_block = soup.find('div', class_="postcard__content postcard__content--primary")
    # print(header_block)
    institute_name = Remove_Unusal_Spaces(header_block.find('h1', class_= "postcard__title"))
    return institute_name