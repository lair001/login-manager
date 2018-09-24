import os


class FileSysUtils:

    @staticmethod
    def validate_directory_path(name, path):
        if os.path.isdir(path):
            return True
        else:
            print(f'Provided {name} directory path does not point to a directory: {path}')
            sys.exit(2)

    @staticmethod
    def validate_file_path(name, path):
        if os.path.isfile(path):
            return True
        else:
            print(f'Provided {name} file path does not point to a file: {path}')
            sys.exit(2)