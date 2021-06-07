from math_series.series import fibonacci, lucas, sum_series
from math_series import __version__

def test_version():
  assert __version__=='0.1.0'
'''
fibonacci test
'''
def test_fibonacci_3():
  expected=2
  actual=fibonacci(3)
  assert expected==actual

def test_fibonacci_7():
  expected=13
  actual=fibonacci(7)
  assert expected==actual


def test_fibonacci_10():
  expected=55
  actual=fibonacci(10)
  assert expected==actual    
  
'''
locus test
'''

def test_lucas_3():
  expected=4
  actual=lucas(3)
  assert expected==actual

def test_lucas_7():
  expected=29
  actual=lucas(7)
  assert expected==actual


def test_lucas_10():
  expected=123
  actual=lucas(10)
  assert expected==actual    
  

'''
sum series test 
'''
def test_sum_series_3():
  expected=11
  actual=sum_series(3,5,3)
  assert expected==actual

def test_sum_series_7():
  expected=79
  actual=sum_series(7,5,3)
  assert expected==actual


def test_sum_series_10():
  expected=395
  actual=sum_series(10,10,1)
  assert expected==actual    
  