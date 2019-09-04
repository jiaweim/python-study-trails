import numpy as np


def test_array_list():
    '''通过list 创建 ndarray'''
    a = np.array([2, 3, 4])
    assert a.size == 3

    b = np.array([1.2, 3.5, 5.1])
    assert b.size == 3
    assert b.dtype == 'float64'


def test_array():
    a = np.array([1, 2, 3])
    assert type(a) == np.ndarray
    assert a.ndim == 1
    assert a.size == 3
    assert a.shape == (3,)
    print(a.dtype)  # dtype vary among different OS


def test_array_tuple():
    d = np.array(((1, 2, 3), (4, 5, 6)))
    assert d.size == 6


def test_array_tuple_list():
    a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    assert a.size == 9


def test_array_2d():
    """创建二维数组"""
    b = np.array([[1.3, 2.4], [0.3, 4.1]])
    assert b.dtype == np.float64
    assert b.dtype == 'float64'
    assert b.ndim == 2
    assert b.size == 4
    assert b.shape == (2, 2)


def test_createWithType():
    b = np.array([[1, 2], [3, 4]], dtype=complex)
    assert b.dtype == np.complex
    print(b)


def test_zeros():
    """
    创建全部包含 0 的数组
    """
    a = np.zeros((3, 3))
    assert a.dtype == np.float64
    # assert a == np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=np.float64)
    print(a)


def test_ones():
    """
    创建全部包含 1 的数组
    """
    a = np.ones((3))
    assert a.dtype == np.float64
    assert a[0] == 1


def test_empty():
    """
    以指定类型创建一个数组，不指定初始值
    """
    a = np.empty([2, 2])
    assert a.shape == (2, 2)