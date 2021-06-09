from jira import JIRA
import config

class TimeEntry(object):
    """ Time Entry """
    def __init__(self):
        self.jira = JIRA(
            basic_auth=(config.username, config.password), 
            options   ={
                         'server': config.server
                       }
)
    def userTimeEnter(self):
    	for detail in config.Ticketdetail:
            self.issue = self.jira.issue(detail['issueid'])
        
            if(self.issue.fields.timetracking.remainingEstimate): # checking the remaining estimation.
                comment = self.jira.add_comment(self.issue, detail['commoncomment'], visibility={"type": "role", 
                	                            "value":"ZeO Users"}, "customfield_10300" : "2019-12-23T14:08:00.000-0500", #working date time picker field
)
                worklog = self.jira.add_worklog(self.issue, timeSpent=detail['timespent'],comment=detail['worklogcomment'])
                self.issue.fields.timetracking.author=detail['author']
            else:
                with open("nontrackedticket.txt", "a") as myfile:
                    myfile.write("No Time remainingEstimate on %s" %detail[issueid])    
                                              
           
    print "Time Entry Completed"    


 



if __name__ == '__main__':
    timeentry = TimeEntry()
    timeentry.userTimeEnter()
