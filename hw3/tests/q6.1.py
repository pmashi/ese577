OK_FORMAT = True

test = {   'name': 'q6.1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> def super_simple_separable():\n'
                                               '...     X = np.array([[2, 5], [3, 2], [9, 6], [12, 5]])\n'
                                               '...     y = np.array([[1, 0, 1, 0]]).T\n'
                                               '...     return (X, y)\n'
                                               '>>> sep_e_separator = (np.array([[-0.40338351], [1.1849563]]), np.array([[-2.26910091]]))\n'
                                               '>>> x_1, y_1 = super_simple_separable()\n'
                                               '>>> th1, th1_0 = sep_e_separator\n'
                                               '>>> ans = llc_obj_61(x_1, y_1, th1, th1_0, 0.1)\n'
                                               '>>> np.isclose(ans, 0.3739416910005669).item() and ans.shape == (1, 1)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> def super_simple_separable():\n'
                                               '...     X = np.array([[2, 5], [3, 2], [9, 6], [12, 5]])\n'
                                               '...     y = np.array([[1, 0, 1, 0]]).T\n'
                                               '...     return (X, y)\n'
                                               '>>> sep_e_separator = (np.array([[-0.40338351], [1.1849563]]), np.array([[-2.26910091]]))\n'
                                               '>>> x_1, y_1 = super_simple_separable()\n'
                                               '>>> th1, th1_0 = sep_e_separator\n'
                                               '>>> ans = llc_obj_61(x_1, y_1, th1, th1_0, 0.0)\n'
                                               '>>> np.isclose(ans, 0.21725772209560584).item() and ans.shape == (1, 1)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
