"""
large_file_reader.py : Utility for reading the large file in chunks.

"""
import os

def read_file_in_chunks(filename, chunk_size = 1000):
    '''
    This generator function which will take the input file and read it in small chunks
    The file is read in chunks so it can handle the large files for reading

    The input chunk_size is used while reading the file.
    '''
    assert os.path.exists(filename), "The given file %s is not exists"%filename
    with open(filename, 'r')as fp:
        data = "some string"
        while data:
            data = fp.read(chunk_size)
            yield data

#usage
filename = r"some file path"
for data in read_file_in_chunks(filename):
    print data