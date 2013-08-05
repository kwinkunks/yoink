"""Test for correctness of color distance functions"""
from os.path import abspath, dirname, join as pjoin

import numpy as np
from numpy.testing import assert_allclose

from yoink.delta_e import (deltaE_cie76,
                           deltaE_ciede94,
                           deltaE_ciede2000,
                           deltaE_cmc)


def test_ciede2000_dE():
    data = load_ciede2000_data()
    N = len(data)
    lab1 = np.zeros((N, 3))
    lab1[:, 0] = data['L1']
    lab1[:, 1] = data['a1']
    lab1[:, 2] = data['b1']

    lab2 = np.zeros((N, 3))
    lab2[:, 0] = data['L2']
    lab2[:, 1] = data['a2']
    lab2[:, 2] = data['b2']

    dE2 = deltaE_ciede2000(lab1, lab2)

    assert_allclose(dE2, data['dE'], rtol=1.e-4)


def load_ciede2000_data():
    dtype = [('pair', int),
             ('1', int),
             ('L1', float),
             ('a1', float),
             ('b1', float),
             ('a1_prime', float),
             ('C1_prime', float),
             ('h1_prime', float),
             ('hbar_prime', float),
             ('G', float),
             ('T', float),
             ('SL', float),
             ('SC', float),
             ('SH', float),
             ('RT', float),
             ('dE', float),
             ('2', int),
             ('L2', float),
             ('a2', float),
             ('b2', float),
             ('a2_prime', float),
             ('C2_prime', float),
             ('h2_prime', float),
             ]

    # note: ciede_test_data.txt contains several intermediate quantities
    path = pjoin(dirname(abspath(__file__)), 'ciede2000_test_data.txt')
    return np.loadtxt(path, dtype=dtype)


def test_cie76():
    data = load_ciede2000_data()
    N = len(data)
    lab1 = np.zeros((N, 3))
    lab1[:, 0] = data['L1']
    lab1[:, 1] = data['a1']
    lab1[:, 2] = data['b1']

    lab2 = np.zeros((N, 3))
    lab2[:, 0] = data['L2']
    lab2[:, 1] = data['a2']
    lab2[:, 2] = data['b2']

    dE2 = deltaE_cie76(lab1, lab2)
    oracle = np.array([
        4.00106328, 6.31415011, 9.1776999, 2.06270077, 2.36957073,
        2.91529271, 2.23606798, 2.23606798, 4.98000036, 4.9800004,
        4.98000044, 4.98000049, 4.98000036, 4.9800004, 4.98000044,
        3.53553391, 36.86800781, 31.91002977, 30.25309901, 27.40894015,
        0.89242934, 0.7972, 0.8583065, 0.82982507, 3.1819238,
        2.21334297, 1.53890382, 4.60630929, 6.58467989, 3.88641412,
        1.50514845, 2.3237848, 0.94413208, 1.31910843
    ])
    assert_allclose(dE2, oracle, rtol=1.e-8)


def test_ciede94():
    data = load_ciede2000_data()
    N = len(data)
    lab1 = np.zeros((N, 3))
    lab1[:, 0] = data['L1']
    lab1[:, 1] = data['a1']
    lab1[:, 2] = data['b1']

    lab2 = np.zeros((N, 3))
    lab2[:, 0] = data['L2']
    lab2[:, 1] = data['a2']
    lab2[:, 2] = data['b2']

    dE2 = deltaE_ciede94(lab1, lab2)
    oracle = np.array([
        1.39503887, 1.93410055, 2.45433566, 0.68449187, 0.6695627,
        0.69194527, 2.23606798, 2.03163832, 4.80069441, 4.80069445,
        4.80069449, 4.80069453, 4.80069441, 4.80069445, 4.80069449,
        3.40774352, 34.6891632, 29.44137328, 27.91408781, 24.93766082,
        0.82213163, 0.71658427, 0.8048753, 0.75284394, 1.39099471,
        1.24808929, 1.29795787, 1.82045088, 2.55613309, 1.42491303,
        1.41945261, 2.3225685, 0.93853308, 1.30654464
    ])
    assert_allclose(dE2, oracle, rtol=1.e-8)


def test_cmc():
    data = load_ciede2000_data()
    N = len(data)
    lab1 = np.zeros((N, 3))
    lab1[:, 0] = data['L1']
    lab1[:, 1] = data['a1']
    lab1[:, 2] = data['b1']

    lab2 = np.zeros((N, 3))
    lab2[:, 0] = data['L2']
    lab2[:, 1] = data['a2']
    lab2[:, 2] = data['b2']

    dE2 = deltaE_cmc(lab1, lab2)
    oracle = np.array([
        1.73873611, 2.49660844, 3.30494501, 0.85735576, 0.88332927,
        0.97822692, 3.50480874, 2.87930032, 6.5783807, 6.57838075,
        6.5783808, 6.57838086, 6.67492321, 6.67492326, 6.67492331,
        4.66852997, 42.10875485, 39.45889064, 38.36005919, 33.93663807,
        1.14400168, 1.00600419, 1.11302547, 1.05335328, 1.42822951,
        1.2548143, 1.76838061, 2.02583367, 3.08695508, 1.74893533,
        1.90095165, 1.70258148, 1.80317207, 2.44934417
    ])

    assert_allclose(dE2, oracle, rtol=1.e-8)


if __name__ == "__main__":
    from numpy.testing import run_module_suite
    run_module_suite()