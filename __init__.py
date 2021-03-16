from mycroft import MycroftSkill, intent_file_handler


class ShowTicketInfo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('info.ticket.show.intent')
    def handle_info_ticket_show(self, message):
        self.speak_dialog('info.ticket.show')


def create_skill():
    return ShowTicketInfo()

