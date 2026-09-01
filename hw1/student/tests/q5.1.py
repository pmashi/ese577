OK_FORMAT = True

test = {   'name': 'q5.1',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])\n'
                                               '>>> Y = np.array([[1], [2], [3], [4]])\n'
                                               '>>> n_splits = 2\n'
                                               '>>> lam = 0.1\n'
                                               '>>> learning_algorithm = lambda X, Y, lam: (np.array([[0.5], [1.0]]), np.array([[0.1]]))\n'
                                               '>>> loss_function = lambda X, Y, th, th0: np.array([[0.01]])\n'
                                               '>>> isinstance(cross_validate_51(X, Y, n_splits, lam, learning_algorithm, loss_function), (float, np.number))\n'
                                               'True',
                                       'failure_message': 'Your function does not return a scalar.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])\n'
                                               '>>> Y = np.array([[1], [2], [3], [4]])\n'
                                               '>>> n_splits = 2\n'
                                               '>>> lam = 0.1\n'
                                               '>>> learning_algorithm = lambda X, Y, lam: (np.array([[0.5], [1.0]]), np.array([[0.1]]))\n'
                                               '>>> loss_function = lambda X, Y, th, th0: np.array([[0.01]])\n'
                                               '>>> np.isclose(cross_validate_51(X, Y, n_splits, lam, learning_algorithm, loss_function), 0.01).item()\n'
                                               'True',
                                       'failure_message': 'Your function does not return the correct value.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
