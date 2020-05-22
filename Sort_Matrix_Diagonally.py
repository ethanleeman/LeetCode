class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        d = collections.defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i-j].append(mat[i][j])
        for k in d.keys():
            d[k].sort()
        for i in reversed(range(len(mat))):
            for j in reversed(range(len(mat[0]))):
                mat[i][j] = d[i-j].pop()
        print mat
        return mat
