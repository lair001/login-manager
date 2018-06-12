import os
from login_manager.libs.file_contents.FileContents import FileContents

class FileContentsByRawValue(FileContents):

    def __init__(self, path):
        assert os.path.isfile(path)
        try:
            self.__path = path
            file = open(path, 'r')
            self.__raw_value = file.read()
            file.close()
        except OSError as err:
            print(err)
            sys.exit(2)

    def get_path(self):
        return self.__path

    def get_contents(self):
        return self.__raw_value

    def update(self, new_raw_value):
        assert isinstance(new_raw_value, str)
        self.__raw_value = new_raw_value
        tmp_file_path = f'{self.get_path()}.tmp'
        tmp_file = open(tmp_file_path, 'w')
        tmp_file.write(new_raw_value)
        tmp_file.close()
        os.replace(tmp_file_path, self.get_path())

    @classmethod
    def get_instance(cls, path):
        return cls(path)

