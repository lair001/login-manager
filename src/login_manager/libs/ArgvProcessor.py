import getopt, sys
from login_manager.libs.ActionStore import ActionStore
from login_manager.libs.resources.Username import Username
from login_manager.libs.actions.Load import Load
from login_manager.libs.actions.Create import Create
from login_manager.libs.actions.DesignateDefault import DesignateDefault


class ArgvProcessor:

    opt_str = "lcdu:h:k:p:fs"

    def __init__(self):
        try:
            self.opts, self.args = getopt.getopt(sys.argv[1:], self.__class__.opt_str)
        except getopt.GetoptError as err:
            print(err)
            sys.exit(2)

    def process_options(self):
        for opt, opt_arg in self.opts:
            getattr(self, "_%s__%s" %(self.__class__.__name__, opt.replace('-', '')))(opt_arg)

    def __l(self, opt_arg):
        ActionStore().add(Load())

    def __c(self, opt_arg):
        ActionStore().add(Create())

    def __d(self, opt_arg):
        ActionStore().add(DesignateDefault())

    def __u(self, opt_arg):
        ActionStore().execute(Username(), opt_arg)

    def __h(self, opt_arg):
        print("host name")

    def __k(self, opt_arg):
        print("key file name")

    def __p(self, opt_arg):
        print("profile file name")

    def __f(self, opt_arg):
        print("user folders and files")

    def __s(self, opt_arg):
        print("sshing into server")
