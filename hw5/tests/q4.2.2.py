OK_FORMAT = True

test = {   'name': 'q4.2.2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> relu = ReLU_422()\n'
                                               '>>> ans = relu.forward(X_sss)\n'
                                               '>>> expected = np.array([[2, 5], [3, 2], [9, 6], [12, 5]])\n'
                                               '>>> np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> relu = ReLU_422()\n'
                                               '>>> _ = relu.forward(X_sss)\n'
                                               '>>> dLdA = np.array([[1, 1, 0, 0], [2, 0, 1, 0]]).T\n'
                                               '>>> ans = relu.backward(dLdA)\n'
                                               '>>> expected = np.array([[1, 2], [1, 0], [0, 1], [0, 0]])\n'
                                               '>>> np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
