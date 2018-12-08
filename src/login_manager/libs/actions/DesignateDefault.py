from login_manager.libs.actions.Action import Action


class DesignateDefault(Action):

    @property
    def type(self):
        return "designate_default"
