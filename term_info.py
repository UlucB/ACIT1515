'''
Final Exam - Question 3 - Bonus
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


def seek_term():
    '''
    seeks term_id from user
    '''
    term_id = input("Please select term: ")
    return term_id


def print_term_info(term_id, file):
    '''
    using user input of term number, returns a printout of the course information for that term
    
    Args: term_id, file to be searched
    
    Return: printout of the course info based on term
    '''
    try:
        found_term = list()
        for i in range(0, len(file)):
            line = file[i].split(',')
            file_term = line[2]
            if file_term==term_id:
                found_term.append(line[0] + ' ' + line[1])
        for i in range(0, len(found_term)):
            print(f"\t{found_term[i]}")
        if len(found_term)<1:
            raise Exception
    except:
        print_term_info(seek_term(), file)


if __name__ == "__main__":
    file = read_file('./course_data.csv')
    term_id = seek_term()
    print_term_info(term_id, file)
