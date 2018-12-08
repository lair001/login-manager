from login_manager.libs.actions.Action import Action


class Load(Action):

    @property
    def type(self):
        return "load"
