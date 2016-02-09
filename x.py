# -*- coding: utf-8 -*-
import xml.etree.ElementTree as etree
import urllib.request
import os.path


def returnScsIdtf(idGroup, nameSubjectAndType):
    if (idGroup == "321"):
        return dict321[nameSubjectAndType]
    # elif(idGroup=="421"):
    #     pass
    else:
        print("AAAAAAAAAAAAAAAA you have to check idGRoup in func returnScsIdtf")


def writeConturs():
    # nameSCSI="321701_"+day+id;
    # f=open(nameSCSI,"w")
    nameSubject = predmet.find("subject").text
    if (nameSubject != "СпецПодг" and nameSubject != "ФизК"):
        teacher = predmet.find("employee")
        teacherId = teacher.find("id").text
        typeSubject = predmet.find("lessonType").text
        shortNameGroupInt = int(int(groupes[0]) // 1000)

        path = "files/"
        time = predmet.find("lessonTime").text
        numberPair = numbersPairs[time]
        nameContur = "spring2016" + "G" + str(
            shortNameGroupInt) + nameSubject + "_" + typeSubject + nameDay + numberPair
        nameFile = path + nameContur
        # print(nameFile)
        nameFileScs = nameFile + ".scs"
        nameFileScsI = nameFile + ".scsi"
        smallNameContur = "small" + nameContur
        smallNameFileScsI = path + "small" + nameContur + ".scsi"
        subGroup=predmet.find("numSubgroup").text
        idtfGroup=""
        if(subGroup==0):
            idtfGroup=currentGroup
        elif(subGroup==1):
            idtfGroup=currentGroup+"_"+"1"
        else:
            idtfGroup=currentGroup+"_"+"2"
        if not (os.path.exists(nameFileScs)):  # else мы дописываем только в мелкий контур а scs и большй контур не трогаем
            weeks = predmet.findall("weekNumber")
            fSCS = open(nameFileScs, "w")
            fSCS.write(nameContur + ' = [*^" ' + nameFileScsI + '"*];;\n')
            fSCS.write("spring2016->" + nameContur + ";;")
            fSCS.close()

            fSCSI = open(nameFileScsI, "w")
            fSCSI.write(smallNameContur + ' = [*^" file://' + smallNameFileScsI + ' "*];; \n')
            fSCSI.write(smallNameContur + " => nrel_time_situation: ...\n (*")
            for week in weeks:
                fSCSI.write("->...(*\n")
                fSCSI.write("<-time_point;;\n")
                fSCSI.write("->rrel_number_of_pair:" + numberPair + " ;;\n")
                fSCSI.write("->rrel_day:" + nameDay + ";;\n")
                fSCSI.write("->rrel_week:" + week.text + " ;;\n")
                fSCSI.write(";;*);;\n")

            fSCSI.write("*);;")
            fSCSI.close()
            #             for small contur

            smallFSCSI = open(smallNameFileScsI, "w")
            nameSubjectAndType = nameSubject + "_" + typeSubject
            print(nameSubjectAndType)
            rightNameSubject=returnScsIdtf(str(shortNameGroupInt),nameSubjectAndType)
            print(rightNameSubject)
            smallFSCSI.write(rightNameSubject +"=>nrel_teach:"+teachers[teacherId]+"; \n")
            smallFSCSI.write("<=group"+idtfGroup+";;")
            smallFSCSI.close()

        else:
            print("dopisivaem in small.scsi")
            smallFSCSI = open(smallNameFileScsI, "a")
            nameSubjectAndType = nameSubject + "_" + typeSubject
            print(nameSubjectAndType)
            rightNameSubject=returnScsIdtf(str(shortNameGroupInt),nameSubjectAndType)
            print(rightNameSubject)
            smallFSCSI.write(rightNameSubject +"=>nrel_teach:"+teachers[teacherId]+"; \n")
            smallFSCSI.write("<=group"+idtfGroup+";;")
            smallFSCSI.close()




# xml_distant = urllib.request.urlopen('xml.xml')   #http://www.bsuir.by/schedule/rest/schedule/21010
groupes = ("321701", "321702", "321703")
teachers = {"504529": "parkalov",
            "502183": "shunja",
            "504551": "rusetckii",
            "500393": "stepanova",
            "500382": "ivash",
            "500384": "kolb",
            "500385": "koronchik",
            "500378": "it dav"
            }
groupesCode = {"321701": "21010", }
numbersPairs = {"08:00-09:35": "FIRST", "09:45-11:20": "SECOND", "11:40-13:15": "THIRD", "13:25-15:00": "FOURTH",
                "15:20-16:55": "FIFTH", "17:05-18:40": "SIXTH"}
dict321 = {"АиПОСиЗИ_ЛР": "laboratory_work_on_apoczi_4_year_education",
           "ЯПИС_ЛР": "laboratory_work_on_language_processors_of_intelligent_systems",
           "ЛОИС_ЛР": "laboratory_work_on_lois_4_year_1",
           "ОИз_ЛР": "laboratory_work_on_analysis_of_image_processing",
           "ПБЗ_ЛР": "laboratory_work_on_pbz_4_year_2",
           "ЕЯзИИС_ЛР": "laboratory_work_on_eyaiis_4_year_1",
           "СтатОИВ_ЛР": "laboratory_work_on_soiv_4_year_education",

           "ЕЯзИИС_ПЗ": "practical_lesson_on_eyaiis_4_year_1",
           "ЛОИС_ПЗ": "practical_lesson_on_lois_4_year_1",

           "СтатОИВ_ЛК": "lectures_on_soiv_4_year_education",
           "ПБЗ_ЛК": "lectures_on_pbz_4_year_2",
           "АиПОСиЗИ_ЛК": "lectures_on_apoczi_4_year_education",
           "ЕЯзИИС_ЛК": "lectures_on_eyaiis_4_year_1",
           "ЯПИС_ЛК": "lectures_on_language_processors_of_intelligent_systems",
           "ЛОИС_ЛК": "lectures_on_lois_4_year_1",
           "ОИз_ЛК": "lectures_on_analysis_of_image_processing" }

# cycle for all groupes
currentGroup=groupes[0]
row = groupesCode["321701"] + ".xml"
print(row)
tree = etree.parse(row)
root = tree.getroot()
allDays = root.findall('scheduleModel')
for day in allDays:  # day == scheduleModel
    nameDay = day.find("weekDay").text
    print("--------" + nameDay)
    predmetsInDay = day.findall("schedule")  # all predmets in day . f.e. in wednesday predmetsInDay=1 (specPodgotovka)
    for predmet in predmetsInDay:
        # print(predmet.find("subject").text)
        writeConturs();
