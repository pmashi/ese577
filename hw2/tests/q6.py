OK_FORMAT = True

test = {   'name': 'q6',
    'points': 20,
    'suites': [   {   'cases': [   {   'code': '>>> def J(x, y, w):\n'
                                               '...     return (w.T @ x - y) ** 2\n'
                                               '>>> def dJ(x, y, w):\n'
                                               '...     return 2 * x @ (w.T @ x - y)\n'
                                               '>>> def rv(values):\n'
                                               '...     return np.array([values])\n'
                                               '>>> def cv(values):\n'
                                               '...     return rv(values).T\n'
                                               '>>> X = np.array([[1, 0, 1], [2, 3, 1], [3, 1, 1]])\n'
                                               '>>> y = np.array([[1], [1], [1]])\n'
                                               '>>> np.random.seed(0)\n'
                                               '>>> w = sgd_6(X, y, J, dJ, cv([1.0, 1.0, 1.0]), lambda i: 0.01, 10000)\n'
                                               '>>> w.shape == (3, 1) and np.allclose(w, cv([0.0, 0.0, 1.0]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> def J(x, y, w):\n'
                                               '...     return (w.T @ x - y) ** 2\n'
                                               '>>> def dJ(x, y, w):\n'
                                               '...     return 2 * x @ (w.T @ x - y)\n'
                                               '>>> def rv(values):\n'
                                               '...     return np.array([values])\n'
                                               '>>> def cv(values):\n'
                                               '...     return rv(values).T\n'
                                               '>>> X = np.array([[1, 0, 1], [2, 3, 5], [3, 1, 2]])\n'
                                               '>>> y = np.array([[0], [0], [0]])\n'
                                               '>>> np.random.seed(0)\n'
                                               '>>> w = sgd_6(X, y, J, dJ, cv([0.5, 0.5, 0.5]), lambda i: 0.01, 10000)\n'
                                               '>>> w.shape == (3, 1) and np.sum(np.abs(w)).item() < 0.0001\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
