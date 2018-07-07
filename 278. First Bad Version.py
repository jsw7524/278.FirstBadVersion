# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return True if version>= 9 else False

class Solution:
    def firstBadVersion(self, n):
        return self.binarySearch(1,n)

    def binarySearch(self, l, r):
        mid = (l + r) // 2
        ft=isBadVersion(mid)
        if (ft == True and  isBadVersion(mid-1)  == False ):
            return mid
        else:
            if (ft  ==  True):
                return self.binarySearch( l, mid-1)
            else:
                return self.binarySearch( mid+1,r)


sln = Solution()
loc=sln.firstBadVersion(13)
assert loc==9