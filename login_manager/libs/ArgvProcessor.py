import getopt, sys


class ArgvProcessor:

    opt_str = "lcdu:h:k:p:fs"

    def __init__(self):
        try:
            self.opts, self.args = \
                getopt.getopt(sys.argv[1:], self.__class__.opt_str)
            self.__opts_to_methods = {
                "-l": self.__l,
                "-c": self.__c,
                "-d": self.__d,
                "-u": self.__u,
                "-h": self.__h,
                "-k": self.__k,
                "-p": self.__p,
                "-f": self.__f,
                "-s": self.__s
            }
        except getopt.GetoptError as err:
            print(err)
            sys.exit(2)

    def process_options(self):
        for opt, opt_arg in self.opts:
            self.__opts_to_methods[opt](opt_arg)

    def __l(self, opt_arg):
        print("loading")

    def __c(self, opt_arg):
        print("creating")

    def __d(self, opt_arg):
        print("designating default")

    def __u(self, opt_arg):
        print("user name")

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
