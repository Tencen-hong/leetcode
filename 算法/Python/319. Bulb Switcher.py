

class Solution:
    def bulbSwitch(self, n):
	    """
		:type n: int
		:rtype: int
		"""

	    '''
		一个开关i被拨动的次数就是i的约数的个数，比如第8个开关，它被拨动了4次，分别在轮数=1,2,4,8时，而1，2，4，8就是8的约数。
		所以题目就变成了求1-n中每个数i的约数个数，如果约数个数是奇数，则开关是开的。
		那么下一步就是求i(i≤n)的约数个数，约数是成对存在的，即2是8的约数，那么
		8÷2=4也是8的约数，其中有一种特殊情况，就是i为完全平方数，比如9跟它的约数3,因此，
		如果i是完全平方数，那么i的约数个数肯定是奇数，如果i不是完全平方数，由于约数成对出现，所以约数个数肯定是偶数。
		这道题就变成了更简单的题目：计算1-n中完全平方数的数目

		为什么对于n以内的数只含有sqrt(n)个完全平方数?8
		首先，所谓的完全平方数：完全平方即用一个整数乘以自己例如1*1，2*2，3*3等，依此类推。
		若一个数能表示成某个整数的平方的形式，则称这个数为完全平方数
		所以我们可以理解，在N以内的最大完全平方因子为sqrt(n)，那么，因为所有的数都能生成一个完全平方数，所以从1到sqrt(n)都能生成一
		个小于等于N的完全平方数，所以我们取N以内的完全平方数个数，只要向下取整求得sqrt (N)即可
		'''

    	return int(math.sqrt(n))
