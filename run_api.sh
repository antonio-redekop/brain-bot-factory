#!/bin/bash

export JIRA_MASTER_ROBOT_ISSUE_KEY="POPS-2632"
export JIRA_MASTER_ROUTING_ISSUE_KEY="POPS-2633"

python -m app.main
