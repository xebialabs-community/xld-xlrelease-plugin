#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import sys
import simplejson as json
from xlrelease.HttpConnection import HttpConnection
from xlrelease.HttpRequest import HttpRequest

PENDING = 'PENDING'
COMPLETED = 'COMPLETED'
IN_PROGRESS = 'IN_PROGRESS'

class XLReleaseClient(object):
    def __init__(self, serverUrl, username = None, password = None, proxyHost = None, proxyPort = None):
        self.httpConnection = HttpConnection(serverUrl, username, password, proxyHost, proxyPort)

    @staticmethod
    def createClient(serverUrl, username = None, password = None, proxyHost = None, proxyPort = None):
        return XLReleaseClient(serverUrl, username, password, proxyHost, proxyPort)

    def isTaskPending(self, taskId, username = None, password = None):
        request = HttpRequest(self.httpConnection, username, password)
        context = '/tasks/%s' % taskId
        response = request.get(context, contentType = 'application/json')
        if response.isSuccessful():
            data = json.loads(response.response)
            status = data["status"]
            print "Current Task with id [%s] is %s." % (taskId, status)
            return status == PENDING
        else:
            print "Failed to get status for task with id: %s" % taskId
            response.errorDump()
            sys.exit(1)

    def isTaskInProgress(self, taskId, username = None, password = None):
        request = HttpRequest(self.httpConnection, username, password)
        context = '/tasks/%s' % taskId
        response = request.get(context, contentType = 'application/json')
        if response.isSuccessful():
            data = json.loads(response.response)
            status = data["status"]
            print "Current Task with id [%s] is %s." % (taskId, status)
            return status == IN_PROGRESS
        else:
            print "Failed to get status for task with id: %s" % taskId
            response.errorDump()
            sys.exit(1)

    def isTaskCompleted(self, taskId, username = None, password = None):
        request = HttpRequest(self.httpConnection, username, password)
        context = '/tasks/%s' % taskId
        response = request.get(context, contentType = 'application/json')
        if response.isSuccessful():
            data = json.loads(response.response)
            status = data["status"]
            print "Current Task with id [%s] is %s." % (taskId, status)
            return status == COMPLETED
        else:
            print "Failed to get status for task with id: %s" % taskId
            response.errorDump()
            sys.exit(1)

    def completeTask(self, taskId, username = None, password = None):
        request = HttpRequest(self.httpConnection, username, password)
        context = '/tasks/%s/complete' % taskId
        body = '{"text":"Completed by XL Deploy"}'
        response = request.post(context, body, contentType = 'application/json')
        if response.isSuccessful() and self.isTaskCompleted(taskId):
            print "Current Task with id [%s] is %s." % (taskId, COMPLETED)
            return True
        else:
            print "Failed to complete task with id: %s" % taskId
            response.errorDump()
            sys.exit(1)