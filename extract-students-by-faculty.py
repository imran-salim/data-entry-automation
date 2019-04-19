import csv

def student_in_faculty(lst, regex):
    for student in lst:
        if student[1] == regex:
            return True
    return False
        
def append_to_csvfile(lst):
    #print "appending student to new csv file"
    if student_in_faculty(lst, 'FCMS'):
        with open('/home/is39/Desktop/testoutput.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerows(lst)
            #print "student has been added to the new csv file"

def process_csvfile():        
    f = open('pycsv.csv')
    csv_f = csv.reader(f)    
    lst = []
    name = ""
    
    for row in csv_f:
        if name == "":
            name = row[0]
            #print name

        if row[0] == name:
            #print row[0]
            #print "match"
            lst.append(row)
        else:
            #print "no match"
            append_to_csvfile(lst)
            del lst[:]
            name = row[0]
            lst.append(row)
            #print lst
            #print name
    append_to_csvfile(lst)
    f.close()
    
process_csvfile()
