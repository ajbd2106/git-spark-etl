import json

from config import Config
from loguru import logger
from .jirafetch import FetchJiraIssues
from .transform import TransformData
from .csvToDataframeApp import extract_data
from .db import Database
import os


def init_script():
    """Extract, transform, and load issues from JIRA to an RDBMS."""
    issues, epics = fetch_jira_issues()
    issues, epics = clean_jira_issues(issues, epics)
    # print(epics)
    # convert to JSON string

    issues.to_csv(r'/Users/ashujha/Data/issue_export_dataframe.csv', index=False, header=True)
    epics.to_csv(r'/Users/ashujha/Data/epic_export_dataframe.csv', index=False, header=True)
    extract_data()


def fetch_jira_issues():
    """Fetch raw JSON data for JIRA issues."""
    jira = FetchJiraIssues(Config)
    issues_json = jira.get_issues()
    epics_json = jira.get_epics()
    print('Fetching issues completed JIRA...')
    return issues_json, epics_json


def clean_jira_issues(issues, epics):
    """Clean data and create pandas DataFrame."""
    logger.info('Transforming JIRA issues to tabular data...')
    transform_data = TransformData()
    issues_df = transform_data.construct_dataframe(issues)
    print('Fetching epics completed JIRA...')
    epics_df = transform_data.construct_dataframe(epics)
    print('Fetching epics completed JIRA...')
    return issues_df, epics_df


def upload_issues(issues, epics):
    """Upload issues table to SQL database."""
    logger.info("Preparing database upload...")
    db = Database(Config)
    epics_upload = db.upload_epics(epics)
    issues_upload = db.upload_issues(issues)
    return epics_upload, issues_upload
