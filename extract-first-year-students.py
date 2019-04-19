import csv
import re

def is_first_year(lst, regex):
    flags = []
    for student in lst:
        match = re.match(regex, student[2])
        if match:
            flags.append(True)
        else:
            flags.append(False)

    paper_count = len(flags)
    lvl100_paper_count = 0

    for f in flags:
        if f == True:
            #print "+1 100 level paper"
            lvl100_paper_count += 1
        #print f
            
    not_lvl100_paper_count = paper_count - lvl100_paper_count
    print "number of 100 level papers: " + str(lvl100_paper_count)
    print "number of papers that are above 100 level: " + str(not_lvl100_paper_count)
    print "total number of papers: " + str(paper_count)
    if lvl100_paper_count >= not_lvl100_paper_count:
        return True
    else:
        return False

def grep_student(lst):
    if is_first_year(lst, '[A-Z]{5}1[0-9]{2}'):
        print "student is a first year student"
        with open('/home/is39/Desktop/firstyears.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerows(lst)
            print "student records have been added to the new file"
    else:
        print "student is not a first year student"

def process_csvfile():
    f = open('testoutput.csv')
    csv_f = csv.reader(f)
    lst = []
    name = ""

    for row in csv_f:
        if name == "":
            print "assigning first name"
            name = row[0]

        if row[0] == name:
            lst.append(row)
            print "appending row to list"
        else:
            print "attempting to grep student"
            grep_student(lst)
            del lst[:]
            print "list has been cleared"
            name = row[0]
            print "assigned a new student"
            lst.append(row)
            print "appending row to list"
    print "final attempt to grep student"
    grep_student(lst)
    f.close()

process_csvfile()
