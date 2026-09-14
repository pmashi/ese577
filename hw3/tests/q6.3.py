OK_FORMAT = True

test = {   'name': 'q6.3',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> def super_simple_separable():\n'
                                               '...     X = np.array([[2, 5], [3, 2], [9, 6], [12, 5]])\n'
                                               '...     y = np.array([[1, 0, 1, 0]]).T\n'
                                               '...     return (X, y)\n'
                                               '>>> sep_e_separator = (np.array([[-0.40338351], [1.1849563]]), np.array([[-2.26910091]]))\n'
                                               '>>> x_1, y_1 = super_simple_separable()\n'
                                               '>>> th, err = llc_min_63(x_1, y_1, 0.0001)\n'
                                               '>>> th.shape == (3, 1) and err.shape == (1, 1) and np.allclose(th, np.array([[-2.03051057, 3.76837138, -2.2234686]]).T) and np.isclose(err, '
                                               'np.array([[0.12496405988662518]])).item()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> def separable_medium():\n'
                                               '...     X = np.array([[2, -1, 1, 1], [-2, 2, 2, -1]]).T\n'
                                               '...     y = np.array([[1, 0, 1, 0]]).T\n'
                                               '...     return (X, y)\n'
                                               '>>> sep_m_separator = (np.array([[2.69231855], [0.67624906]]), np.array([[-3.02402521]]))\n'
                                               '>>> x_2, y_2 = separable_medium()\n'
                                               '>>> th, err = llc_min_63(x_2, y_2, 0.0001)\n'
                                               '>>> th.shape == (3, 1) and err.shape == (1, 1) and np.allclose(th, np.array([[2.73541729, 0.95015945, -2.22013763]]).T) and np.isclose(err, '
                                               'np.array([[0.21613294514553352]])).item()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
