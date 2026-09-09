OK_FORMAT = True

test = {   'name': 'q5.1',
    'points': 8,
    'suites': [   {   'cases': [   {   'code': '>>> def f1(x):\n'
                                               '...     return x[1:2, :] ** 2 + x[2:3, :]\n'
                                               '>>> def df1(x):\n'
                                               '...     x = list(x.squeeze())\n'
                                               '...     return cv([0, 2 * x[1], 1])\n'
                                               '>>> def rv(values):\n'
                                               '...     return np.array([values])\n'
                                               '>>> def cv(values):\n'
                                               '...     return rv(values).T\n'
                                               '>>> x1, fx1 = gd_51(f1, df1, cv([1.0, 1.0, 1.0]), lambda i: 0.1, 1000)\n'
                                               '>>> x1.shape == (3, 1) and np.allclose(x1, cv([1, 0, -99])) and (fx1.shape == (1, 1)) and np.allclose(fx1, -99)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> def f2(x):\n'
                                               '...     return x[0:1, :] * x[1:2, :]\n'
                                               '>>> def df2(x):\n'
                                               '...     x = list(x.squeeze())\n'
                                               '...     return cv([x[1], x[0], 0])\n'
                                               '>>> def rv(values):\n'
                                               '...     return np.array([values])\n'
                                               '>>> def cv(values):\n'
                                               '...     return rv(values).T\n'
                                               '>>> x2, fx2 = gd_51(f2, df2, cv([2.0, 3.0, 4.0]), lambda i: 0.01, 1000)\n'
                                               '>>> (x2.shape == (3, 1) and x2[2] == 4 and (np.abs(x2[0, 0] + x2[1, 0]) < 0.001) and (np.abs(x2[0, 0]) > 10000.0) and (fx2.shape == (1, 1)) and '
                                               '(fx2[0, 0] < -100000000.0)).item()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
