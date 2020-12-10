import unittest
from doy15.fangfa import Calc
from ddt import ddt
from ddt import data
from ddt import unpack
data1 = [
    [1,2,3],
    [-1,-2,-3],
    [5,-2,3],
    [0,5,5]
]
@ddt
class TestCalcAdd(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAdd(self,d,e,f):
        a = d
        b = e
        c = f
        calc = Calc()


        sum = calc.add(a,b)

        self.assertEqual(c,sum)



data2 = [
    [3,2,1],
    [0,4,-4],
    [-4,-5,1],
    [5,-4,9]
]
@ddt
class TestCalcSubt(unittest.TestCase):
    @data(*data2)
    @unpack
    def testSubt(self,g,h,i):
        j = g
        k = h
        l = i
        calc = Calc()

        sum = calc.subt(j,k)

        self.assertEqual(l,sum)



data3 = [
    [3,2,6],
    [0,4,0],
    [-4,-5,20],
    [5,-4,-20]
]
@ddt
class TestCalcMult(unittest.TestCase):
    @data(*data3)
    @unpack
    def testMult(self,m,n,o):
        r = m
        s = n
        t = o
        calc = Calc()

        sum = calc.mult(r,s)

        self.assertEqual(t,sum)


data4 = [
    [6,2,3],
    [4,4,1],
    [20,5,4],
    [100,1,100]
]
@ddt
class TestCalcDivi(unittest.TestCase):
    @data(*data4)
    @unpack
    def testDivi(self,w,x,h):
        u = w
        v = x
        y = h
        calc = Calc()

        sum = calc.divi(u,v)

        self.assertEqual(y,sum)




