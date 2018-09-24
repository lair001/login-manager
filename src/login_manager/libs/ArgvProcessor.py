import getopt, sys
from login_manager.libs.ActionStore import ActionStore
from login_manager.libs.resources.Username import Username


class ArgvProcessor:

    opt_str = "lcdu:h:k:p:fs"

    def __init__(self):
        try:
            self.opts, self.args = getopt.getopt(sys.argv[1:], self.__class__.opt_str)
            self.action_store = ActionStore()
        except getopt.GetoptError as err:
            print(err)
            sys.exit(2)

    def process_options(self):
        for opt, opt_arg in self.opts:
            getattr(self, "_%s__%s" %(self.__class__.__name__, opt.replace('-', '')))(opt_arg)

    def __l(self, opt_arg):
        self.action_store.set_should_load_as_true()

    def __c(self, opt_arg):
        self.action_store.set_should_create_as_true()

    def __d(self, opt_arg):
        self.action_store.set_should_designate_default_as_true()

    def __u(self, opt_arg):
        if self.action_store.should_load():
            Username().load(opt_arg)
        if self.action_store.should_designate_default():
            Username().designate_default(opt_arg)

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
