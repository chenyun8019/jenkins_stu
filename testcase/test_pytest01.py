# coding=utf-8
'''
author:chenyun
date:2022/6/20
describe:
'''
import pytest
def test_01():
    print('test_01')

def test_02():
    print('test_02')

def test_03():
    print('test_03')

if __name__ == '__main__':
    pytest.main(['-v','-s'])