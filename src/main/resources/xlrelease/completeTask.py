import sys
from xlrelease.XLReleaseClientUtil import XLReleaseClientUtil

xlrClient = XLReleaseClientUtil.createXLReleaseClient(deployed.container)
taskId = deployed.getProperty('taskId')
username = deployed.getProperty('username')
password = deployed.getProperty('password')
owner = username if username else deployed.container.getProperty('username')
if taskId and xlrClient.isTaskInProgress(taskId, username, password):
    if xlrClient.assign_task(taskId,owner,username,password):
        print "Assigned task with id [%s] to owner [%s]" % (taskId, owner)
    else:
        print "Failed assigning task with id [%s] to owner [%s]" % (taskId, owner)
        sys.exit(1)
        
    if xlrClient.complete_task(taskId,username,password):
        print "Successful completed task with id: [%s]" % taskId
    else:
        print "Failed completing task"
        sys.exit(1)
else:
    print "Is the task in progress?"
    sys.exit(1)

