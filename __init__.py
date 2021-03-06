from mycroft import MycroftSkill, intent_file_handler
import sqlite3
import random

class ShowTicketInfo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('info.ticket.show.intent')
    def handle_info_ticket_show(self, message):
        conn = sqlite3.connect("cubic.sql") 
        cur = conn.cursor()
    
        cur.execute("SELECT * FROM PassData")
        rows = cur.fetchall()

        #self.speak('Here are the available tickets.')
        
        i=1
        answer = "yes"
        while (answer == "yes"):
            i = 1
            self.speak('Here are the available tickets: ')
            for row in rows:
                cur.execute("SELECT * FROM TransitLine WHERE LineID = ?", (row[3],))
                idrow = cur.fetchone()
                self.speak('Ticket number {} : starts at {}, ends at {}, has an E.T.A of {}, and costs ${}.'.format(i, row[4], row[5], idrow[3], row[6]))
                i += 1

            n = int(self.get_response('These are all the tickets available. Which ticket would you like to select?'))
            m = n
            n = n - 1

            cur.execute("SELECT * FROM PassData LIMIT 1 OFFSET ?", (n,))
            ticket = cur.fetchone()

            cur.execute("SELECT * FROM TransitLine WHERE LineID = ?", (ticket[3],))

            idrow = cur.fetchone()

            self.speak('You have chosen to view following ticket: \n')
            self.speak(' Ticket: {}. Start: {},  End: {},  ETA: {},  Cost: ${}.'.format(m, ticket[4], ticket[5], idrow[3], ticket[6]))
            #ask user what to do after ticket info is displayed
            answer = self.ask_yesno('Would you like to choose another ticket to view? Please say yes or no: ')
            if answer == "yes":
                self.speak('Fetching ticket information...')

        self.speak('Thank you. Closing the ticket viewer...')
        conn.close()
        #self.speak_dialog('info.ticket.show')




def create_skill():
    return ShowTicketInfo()

