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
    createNewFile = 0  # для подгрупп если обе подгруппы в одно время но по разным неделям,как у нас в четверг пбз ЛБ
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
            shortNameGroupInt) + engShortNamesSubject[nameSubject] + "_" + engNameTypeSubject[typeSubject] + \
                     engDay[nameDay] + numberPair
        nameFile = path + nameContur
        # print(nameFile)
        nameFileScs = nameFile + ".scs"
        nameFileScsI = nameFile + ".scsi"
        smallNameContur = "small" + nameContur
        smallNameFileScsI = path + "small" + nameContur + ".scsi"
        subGroup = predmet.find("numSubgroup").text
        idtfGroup = ""
        if (subGroup == "0"):
            idtfGroup = currentGroup
        elif (subGroup == "1"):
            createNewFile = 1
            idtfGroup = currentGroup + "_" + "1"
        else:
            createNewFile = 1
            idtfGroup = currentGroup + "_" + "2"
        if not (
        os.path.exists(nameFileScs)):  # else мы дописываем только в мелкий контур а scs и большй контур не трогаем
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
                fSCSI.write("->rrel_day:" + engDay[nameDay] + ";;\n")
                fSCSI.write("->rrel_week:" + week.text + " ;;\n")
                fSCSI.write(";;*);;\n")

            fSCSI.write("*);;")
            fSCSI.close()
            #             for small contur

            smallFSCSI = open(smallNameFileScsI, "w")
            nameSubjectAndType = nameSubject + "_" + typeSubject
            print(nameSubjectAndType)
            rightNameSubject = returnScsIdtf(str(shortNameGroupInt), nameSubjectAndType)
            print(rightNameSubject)
            smallFSCSI.write(rightNameSubject + "=>nrel_teach:" + teachers[teacherId] + "; \n")
            smallFSCSI.write("<=group" + idtfGroup + ";;\n\n")
            smallFSCSI.close()

        else:
            if (createNewFile == 0):
                print("dopisivaem in small.scsi")
                smallFSCSI = open(smallNameFileScsI, "a")
                nameSubjectAndType = nameSubject + "_" + typeSubject
                print(nameSubjectAndType)
                rightNameSubject = returnScsIdtf(str(shortNameGroupInt), nameSubjectAndType)
                print(rightNameSubject)
                smallFSCSI.write(rightNameSubject + "=>nrel_teach:" + teachers[teacherId] + "; \n")
                smallFSCSI.write("<=group" + idtfGroup + ";;\n\n")
                smallFSCSI.close()
            elif (createNewFile == 1):
                smallNameContur = "small" + nameContur + idtfGroup
                smallNameFileScsI = path + smallNameContur + ".scsi"
                nameFileScsI = nameFile + idtfGroup + ".scsi"
                weeks = predmet.findall("weekNumber")
                nameFileScs = nameFile + idtfGroup + ".scs"
                fSCS = open(nameFileScs, "w")
                fSCS.write(nameContur + idtfGroup + ' = [*^" ' + nameFileScsI + '"*];;\n')
                fSCS.write("spring2016->" + nameContur + idtfGroup + ";;")
                fSCS.close()

                fSCSI = open(nameFileScsI, "w")
                fSCSI.write(smallNameContur + ' = [*^" file://' + smallNameFileScsI + ' "*];; \n')
                fSCSI.write(smallNameContur + " => nrel_time_situation: ...\n (*")
                for week in weeks:
                    fSCSI.write("->...(*\n")
                    fSCSI.write("<-time_point;;\n")
                    fSCSI.write("->rrel_number_of_pair:" + numberPair + " ;;\n")
                    fSCSI.write("->rrel_day:" + engDay[nameDay] + ";;\n")
                    fSCSI.write("->rrel_week:" + week.text + " ;;\n")
                    fSCSI.write(";;*);;\n")

                fSCSI.write("*);;")
                fSCSI.close()
                #             for small contur

                smallFSCSI = open(smallNameFileScsI, "w")
                nameSubjectAndType = nameSubject + "_" + typeSubject
                print(nameSubjectAndType)
                rightNameSubject = returnScsIdtf(str(shortNameGroupInt), nameSubjectAndType)
                print(rightNameSubject)
                smallFSCSI.write(rightNameSubject + "=>nrel_teach:" + teachers[teacherId] + "; \n")
                smallFSCSI.write("<=group" + idtfGroup + ";;\n\n")
                smallFSCSI.close()
            else:
                print("c---------------------------------------------")


# xml_distant = urllib.request.urlopen('xml.xml')   #http://www.bsuir.by/schedule/rest/schedule/21010
# groupes = ("321701", "321702", "321703")
groupes = ("421701", "421702", "421703")
teachers = {"504529": "Parkalov_Alexey_Viktorovich",
            "502183": "shunkevich_d_v",
            "504551": "rusetski_k_v",
            "500393": "Stepanova_Margarita_Dmitrievna",
            "500382": "Ivashenko_Valerian_Petrovich",
            "500384": "Kolb_Dmitry_Grigorxevich",
            "500385": "Koronchik_Denis_Nikolaevich",
            "500378": "Davydenko_Irina_Timofeevna ",
            "502185": "Romanov_Vladimir_Ilxich",
            "500381": "Zakharov_Vladimir_Vladimirovich",
            "504356": "shatilo nikolai ",
            "505991": "korotkevich dmitrii alersandrovich ",
            "500368": " pavlovec juri",
            "500511": "belskii aleksei ",
            "504528": "Zhukov_Ivan_Ivanovich",
            "500377": "Gulyakina_Natalia_Anatolevna",
            "504367": "adamovich_vadim ",
            "504358": "Stoler denis ",
            "500375" : "Golenkov_Vladimir_Vasilevich ",
            "502097" : "Grakova_Natalia_Viktorovna"
            }
engShortNamesSubject = {"АиПОСиЗИ": "aipos",
                        "ЯПИС": "japis",
                        "ЛОИС": "lois",
                        "ОИз": "oiz",
                        "ПБЗ": "pbz",
                        "ЕЯзИИС": "ejaiis",
                        "СтатОИВ": "StatOiv"
                        }
engNameTypeSubject = {"ЛР": "",
                      "ПЗ": "",
                      "ЛК": "",
                      }
engDay = {"Понедельник": "Monday",
          "Вторник": "Tuesday",
          "Среда": "Wednesday",
          "Четверг": "Thursday",
          "Пятница": "Friday",
          "Суббота": "Saturday",
          }
groupesCode = {"321701": "21010", "321702": "21079", "321703": "21080", "421701": "21139", "421702": "21207",
               "421703": "21208"}
# groupesCode = {"421701": "21139", "421702": "21207", "421703": "21208" }
numbersPairs = {"08:00-09:35": "first_pair", "09:45-11:20": "second_pair", "11:40-13:15": "third_pair",
                "13:25-15:00": "fourth_pair",
                "15:20-16:55": "fifth_pair", "17:05-18:40": "sixth_pair", "18:45-20:20": "seventh_pair",
                "20:25-22:00": "eigthth_pair"}
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
           "ОИз_ЛК": "lectures_on_analysis_of_image_processing"}
# 421701 -21139
# 421702 - 21207
# 421703- 21208
# cycle for all groupes
# var=0
for var in groupes:
    currentGroup = var
    row = groupesCode[var] + ".xml"
    print(row)
    tree = etree.parse(row)
    root = tree.getroot()
    allDays = root.findall('scheduleModel')
    for day in allDays:  # day == scheduleModel
        nameDay = day.find("weekDay").text
        print("--------" + nameDay)
        predmetsInDay = day.findall(
            "schedule")  # all predmets in day . f.e. in wednesday predmetsInDay=1 (specPodgotovka)
        for predmet in predmetsInDay:
            # print(predmet.find("subject").text)
            writeConturs();
