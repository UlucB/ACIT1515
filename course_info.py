'''
Final Exam - Question 3
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


def seek_course():
    '''
    seeks course_id from user
    '''
    course_id = input("Please enter a course id: ")
    return course_id.upper()


def print_course_info(course_id, file):
    '''
    using user input of course number, returns a printout of the course information for that course
    
    Args: course_id, file to be searched
    
    Return: printout of the course info based on ID
    '''
    try:
        found_course = ()
        for i in range(0, len(file)):
            line = file[i].split(',')
            file_course_id = line[0]
            if file_course_id==course_id:
                found_course = file[i]
                break
        found_course = found_course.split(',')
        print("Course ID: {}" .format(found_course[0]))
        print(f"\tCourse Title: {found_course[1]}")
        print(f"\tTerm: {found_course[2]}")
        print(f"\tCredits: {found_course[3]}")

        if len(found_course[4])>0:
            prereqs = found_course[4].split(';')
        else:
            prereqs = []
        print(f"\tPrerequisites: {prereqs}")

        if len(found_course[5]) < 8:
            coreqs = []
        else:
            coreqs = [found_course[5].strip()]
        print(f"\tCorequisites: {coreqs}")

    except:
        print_course_info(seek_course(), file)


if __name__ == "__main__":
    file = read_file('./course_data.csv')
    course_id = seek_course()
    print_course_info(course_id, file)
