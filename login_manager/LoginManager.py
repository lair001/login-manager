from login_manager.libs.ArgvProcessor import ArgvProcessor
from login_manager.libs.resources.UserConfig import UserConfig


class LoginManager:

    def __init__(self):
        pass

    def run(self):
        UserConfig()
        ArgvProcessor().process_options()
