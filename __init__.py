from mycroft import MycroftSkill, intent_file_handler


class MathTuter(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tuter.math.intent')
    def handle_tuter_math(self, message):
        self.speak_dialog('tuter.math')


def create_skill():
    return MathTuter()

