from login_manager.libs.actions.Action import Action


class Create(Action):

    @property
    def type(self):
        return "create"
