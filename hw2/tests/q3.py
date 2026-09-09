OK_FORMAT = True

test = {   'name': 'q3',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> x = np.array([[1], [2]])\n'
                                               '>>> theta = np.array([[0.1], [0.2]])\n'
                                               '>>> theta_0 = np.array([[0.5]])\n'
                                               '>>> y = np.array([[1.0]])\n'
                                               '>>> lam = 0.1\n'
                                               '>>> n = 10\n'
                                               '>>> isinstance(f_3(x, y, theta, theta_0, lam, n), np.ndarray) and f_3(x, y, theta, theta_0, lam, n).shape == (1, 1)\n'
                                               'True',
                                       'failure_message': 'Did not return a 1 x 1 array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> x = np.array([[1], [2]])\n'
                                               '>>> theta = np.array([[0.1], [0.2]])\n'
                                               '>>> theta_0 = np.array([[0.5]])\n'
                                               '>>> y = np.array([[1.0]])\n'
                                               '>>> lam = 0.1\n'
                                               '>>> n = 10\n'
                                               '>>> np.isclose(f_3(x, y, theta, theta_0, lam, n), np.array([[0.0005]])).item()\n'
                                               'True',
                                       'failure_message': 'Did not return a 1 x 1 array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
