'''
Final Exam - Question 2
Written by: Luke Birol
Date: Dec 8, 2021
'''


def read_file(file_name):
    '''
    opens a file, returns lines in txt file as list
    
    Args: a name of a text file
    
    Return: list containing lines from the file
    '''
    file = open(file_name)
    file_lines = file.readlines()
    return file_lines


def write_stu_avg(file_lines):
    '''
    parses lines from a file for student grades for each course and computes total average, writes it to a new file
    
    Args: lines from a txt file with student grades
    
    Return: new file with student total averages
    '''
    file = open('student_avgs.txt', 'w')
    for i in range(1, len(file_lines)):
        info = file_lines[i].split()
        stu_num=info[0]
        grade1=int(info[1])
        grade2=int(info[2])
        grade3=int(info[3])
        grade4=int(info[4])
        grade5=int(info[5])
        grade6=int(info[6])
        grade7=int(info[7])
        avg_grade = (grade1 +  grade2+ grade3 + grade4+grade5+grade6+grade7)/7
        file.write("{} {:.0f}\n" .format(stu_num, avg_grade))
    file.close()


def write_course_avg(file_lines):
    '''
    parses file to determine course averages and writes the averages to a file named course_avgs.txt
    
    Args: lines from a txt file
    
    Return: new file with averages indicated
    '''
    total_ACIT1420=0
    total_ACIT1515=0
    total_ACIT1620=0
    total_ACIT1630=0
    total_COMM1116=0
    total_MATH1310=0
    total_ORGB1100=0
    for i in range(1, len(file_lines)):
        info = file_lines[i].split()

        grade1=int(info[1])
        total_ACIT1420 += grade1

        grade2=int(info[2])
        total_ACIT1515 += grade2

        grade3=int(info[3])
        total_ACIT1620 += grade3

        grade4=int(info[4])
        total_ACIT1630 += grade4

        grade5=int(info[5])
        total_COMM1116 += grade5
     
        grade6=int(info[6])
        total_MATH1310 += grade6

        grade7=int(info[7])
        total_ORGB1100 += grade7

    file = open('course_avgs.txt', 'w')
    file.write("ACIT1420 {:.0f}\n" .format(total_ACIT1420/(len(file_lines)-1)))
    file.write("ACIT1515 {:.0f}\n" .format(total_ACIT1515/(len(file_lines)-1)))
    file.write("ACIT1620 {:.0f}\n" .format(total_ACIT1620/(len(file_lines)-1)))
    file.write("ACIT1630 {:.0f}\n" .format(total_ACIT1630/(len(file_lines)-1)))
    file.write("COMM1116 {:.0f}\n" .format(total_COMM1116/(len(file_lines)-1)))
    file.write("MATH1310 {:.0f}\n" .format(total_MATH1310/(len(file_lines)-1)))
    file.write("ORGB1100 {:.0f}\n" .format(total_ORGB1100/(len(file_lines)-1)))
    file.close()
    return file
    

if __name__ == "__main__":
    file_lines = read_file('./grades.txt')
    write_stu_avg(file_lines)
    write_course_avg(file_lines)