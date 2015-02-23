#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import sys
from xlrelease.util import XLReleaseClientUtil

xlrClient = XLReleaseClientUtil.createXLReleaseClient(deployed.container)
taskId = deployed.getProperty('taskId')
username = deployed.getProperty('username')
password = deployed.getProperty('password')
if taskId and xlrClient.isTaskInProgress(taskId, username, password):
    if xlrClient.completeTask(taskId,username,password):
        print "Successful completed task with id: %s" % taskId
    else:
        print "Failed completing task"
        sys.exit(1)
else:
    print "Is the task in progress?"
    sys.exit(1)

