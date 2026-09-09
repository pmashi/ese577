OK_FORMAT = True

test = {   'name': 'q5.2',
    'points': 8,
    'suites': [   {   'cases': [   {   'code': '>>> def f1(x):\n'
                                               '...     return x[1:2, :] ** 2 + x[2:3, :]\n'
                                               '>>> num_df1 = make_num_grad_fn_52(f1)\n'
                                               '>>> def rv(values):\n'
                                               '...     return np.array([values])\n'
                                               '>>> def cv(values):\n'
                                               '...     return rv(values).T\n'
                                               '>>> num_dfx1 = num_df1(cv([1.0, 1.0, 1.0]))\n'
                                               '>>> callable(num_df1) and num_dfx1.shape == (3, 1) and np.allclose(num_dfx1, cv([0.0, 2.0, 1.0]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> def f2(x):\n'
                                               '...     return x[0:1, :] * x[1:2, :]\n'
                                               '>>> num_df2 = make_num_grad_fn_52(f2)\n'
                                               '>>> def rv(values):\n'
                                               '...     return np.array([values])\n'
                                               '>>> def cv(values):\n'
                                               '...     return rv(values).T\n'
                                               '>>> num_dfx2 = num_df2(cv([2.0, 3.0, 4.0]))\n'
                                               '>>> callable(num_df2) and num_dfx2.shape == (3, 1) and np.allclose(num_dfx2, cv([3.0, 2.0, 0.0]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
