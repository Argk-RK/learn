# Karmic Time Entry Automation.

 Drop the configuration on the config file with the ticket,comments and timeentry hours and scheduled on your local machine with pre-defined bat file. This will automate the time entry.

The general comment will explain in detail with Zeomega internal user restriction and worklog comment will be added separately.

If any of the tikcet does not have the enough estimation remaining time. Those ticket details will be tracked on the different text file under same director. This will help us to request the team to increase the time estimation.

## Getting Started

These instructions will get you a copy of the project up and task scheduled on your local machine to automate the time entry.

### Prerequisites

```
* Python 2x

* jira module

```

### Installing

**pip install jira**


```
Give an config example 

Ticketdetail = [{'issueid':'JO-465','commoncomment':'commoncomment testing from config','timespent':'5h',
                 'worklogcomment':'configworklog comment','author':'rpandi@zeomega.com'},
                 {'issueid':'JO-272','commoncomment':'commoncomment testing from config','timespent':'5h',
                 'worklogcomment':'scheduler comment','author':'rpandi@zeomega.com'},

                 ]

 ```                



## Versioning

git@git.zeomega.com:rpandi/Karmic-TimeEntryAutomation.git/mater

## Authors

* **Rajesh Kanna Pandi** -krajesh@zeomega.com