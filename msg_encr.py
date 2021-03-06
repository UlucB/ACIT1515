'''
Final Exam - Question 1
Written by: Luke Birol
Date: Dec 8, 2021
'''

import sys
import caesar_cipher

def read_file(file_name):
    '''
    opens a file, returns lines in txt file as list
    
    Args: a name of a text file
    
    Return: list containing lines from the file
    '''
    file = open(file_name)
    file_lines = file.readlines()

    return file_lines

def write_file(file_name, message):
    '''
    takes file name given and creates a new file with that name
    writes the message given by encrypt/decrypt function by appending to the file
    
    Args: name of the file to create, message generated by encrypt/decrypt
    
    Return: text file with the name specified and content
    '''
    new_file = open(file_name, 'a')
    new_file.write(message)
    new_file.close()
    return new_file

if __name__ == "__main__":
    encryption_cypher = caesar_cipher.generate_cipher()
    decryption_cypher = caesar_cipher.generate_rev_cypher(encryption_cypher)
    try:
        message = read_file(sys.argv[2])
        try:
            if sys.argv[1] == '-e':
                for line in message:
                    new_line = caesar_cipher.encode_message(encryption_cypher, line)
                    write_file(sys.argv[3], new_line)
            elif sys.argv[1] == '-d':
                for line in message:
                    new_line  = caesar_cipher.encode_message(decryption_cypher, line)
                    write_file(sys.argv[3], new_line)
            else:
                raise ValueError
        except ValueError:
            print('Please specify a valid operation "-e" to encrypt or "-d" to decrypt')
    except FileNotFoundError:
        print('Input file not found. Please specify an existing input file')
    except:
        print('Please specify an operation "-e" to encrypt or "-d" to decrypt, an input file, and an output file')
    