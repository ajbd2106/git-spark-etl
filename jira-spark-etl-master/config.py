"""Project configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:

    # Database config
    db_uri = "mysql+pymysql://root:hadoop@localhost:3306/jira"
    db_epic_table = "JiraEpic"
    db_jira_table = "JiraIssue"

    # JIRA config
    jira_username = "jhaashish21@gmail.com"
    jira_api_key = "zt4n9nzx1qOWhNLfAgFU903E"
    jira_endpoint = "http://ashtan21.atlassian.net/rest/api/2/search"
    jira_issues_jql = "project = ASHTAN"
    jira_issues_fields = ""
    jira_epics_jql = "project = ASHTAN AND type = Epic"
    jira_epics_fields = ""
