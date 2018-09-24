import os
import sys
from pathlib import Path
from login_manager.libs.resources.Resource import Resource
from login_manager.libs.file_contents.FileContentsByFields import FileContentsByFields
from login_manager.libs.utils.FileSysUtils import FileSysUtils


class UserConfig(Resource):

    user_directory_name = 'lgn'
    user_directory_path = os.path.join(Path.home(), user_directory_name)
    user_config_file_name = 'lgn.conf'
    user_config_file_path = os.path.join(user_directory_path, user_config_file_name)

    __user_config_file_field_names = ['default_keys_directory_path',
                                      'default_profiles_directory_path',
                                      'default_profile_file_name']

    def __init__(self):
        self.load(self.__class__.user_config_file_path)

    def load(self, user_config_file_path):
        self.__user_config_file_contents = self.__class__.validate(self.__class__.user_config_file_path)
        user_config_file_fields = self.__user_config_file_contents.get_contents()
        for field_name in self.__class__.__user_config_file_field_names:
            setattr(self, field_name, user_config_file_fields[field_name]['value'])
        self.keys_directory_path = self.default_keys_directory_path
        self.profiles_directory_path = self.default_profiles_directory_path

    def create(self):
        super().create()

    def designate_default(self):
        super().designate_default()

    @classmethod
    def is_valid(cls, user_config_file_fields):
        assert isinstance(user_config_file_fields, dict)
        for field_name in cls.__user_config_file_field_names:
            if field_name not in user_config_file_fields:
                return False
        return True

    @classmethod
    def validate(cls, user_config_file_path):
        FileSysUtils.validate_file_path('user configuration file', user_config_file_path)
        user_config_file_contents = FileContentsByFields.get_instance(user_config_file_path)
        user_config_file_fields = user_config_file_contents.get_contents()

        if cls.is_valid(user_config_file_fields):
            FileSysUtils.validate_directory_path('keys',
                                     user_config_file_fields['default_keys_directory_path']['value'])
            FileSysUtils.validate_directory_path('profiles',
                                     user_config_file_fields['default_profiles_directory_path']['value'])
            return user_config_file_contents

        print(f'Provided user configuration file is invalid: {user_config_file_path}')
        sys.exit(2)







