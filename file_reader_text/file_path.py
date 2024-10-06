# class FilePath():
#     def __init__(self, slip):
#         self.slip = slip
#         self.file_path = 'file_reader_text/some_file.txt'

#     def show_path(self):
#         return self.file_path
    
# infor = FilePath('1')
# print(infor.__dict__)
# print(infor.show_path())


# class FilePath():
#     def show_path(file_path='file_reader_text/some_file.txt'):
#         return file_path
    
# print((FilePath().show_path()).__dict__)


def show_path(file_path='file_reader_text/some_file.txt'):
    return file_path
    
print(show_path())