class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        novoIp = address.replace('.','[.]')
        return novoIp
        