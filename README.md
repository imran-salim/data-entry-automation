# data-entry-automation
Two scripts that I hacked together to automate two data entry tasks.

These scripts were used to manipulate CSV files which were converted from Excel files. The purpose was to extract data from the CSV files with the use of the interpreted language python.

'extract-first-year-students.py' was used to get all the first-year students. A column in the CSV file denoted which students were first-year students and this made it possible to copy the first-year students out of the file and store it in another CSV file by using regular expressions.

'extract-students-by-faculty.py' was used to get all the students belonging to either of the two faculties: 'FCMS' or 'FSEN'. Faculty of Computing and Mathematical Sciences, and Faculty of Science and Engineering. A column in the CSV file denoted which faculty the student was in. I specified which faculty that I wanted to copy the students from within in the CSV file, and this then stored the students in the specified faculty in another CSV file.
