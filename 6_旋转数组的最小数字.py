# -*- coding: cp936 -*-
class Solution:
    def minNumberInRotateArray(self,rotateArray):           #˳��������Ӷ�ΪO(n)
        if not rotateArray:
            return 0
        for i in range(len(rotateArray)-1):
            if rotateArray[i] > rotateArray[i+1]:           #���ֽ���
                return rotateArray[i+1]
        return rotateArray[0]                               #��������������ֵ���ߵ�Ԫ������

if __name__ == "__main__":
    rotateArray1 = [3,4,5,1,2]
    rotateArray2 = [2,2,2,2,2]
    rotateArray3 = [3]
    solution = Solution()
    print solution.minNumberInRotateArray(rotateArray1)
    print solution.minNumberInRotateArray(rotateArray2)
    print solution.minNumberInRotateArray(rotateArray3)
   
