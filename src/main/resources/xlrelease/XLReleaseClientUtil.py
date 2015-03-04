#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from xlrelease.XLReleaseClient import XLReleaseClient


class XLReleaseClientUtil(object):

    @staticmethod
    def createXLReleaseClient(container):
        client = XLReleaseClient.createClient(container.getProperty("serverUrl"), container.getProperty("username"), container.getProperty("password"), container.getProperty('proxyHost'), container.getProperty('proxyPort'))
        return client

