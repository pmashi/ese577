OK_FORMAT = True

test = {   'name': 'q4.1',
    'points': 20,
    'suites': [   {   'cases': [   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> linear = Linear_41(2, 3)\n'
                                               '>>> ans = linear.forward(X_sss)\n'
                                               '>>> expected = np.array([[10.41750064, 7.16872235, -2.07105455], [6.91122168, 3.48998746, 0.69413716], [20.73366505, 10.46996239, 2.08241149], '
                                               '[22.8912344, 9.9982611, 4.84966811]])\n'
                                               '>>> np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> linear = Linear_41(2, 3)\n'
                                               '>>> linear.W0 = np.array([[1, 1, 1]])\n'
                                               '>>> ans = linear.forward(X_sss)\n'
                                               '>>> expected = np.array([[11.41750064, 8.16872235, -1.07105455], [7.91122168, 4.48998746, 1.69413716], [21.73366505, 11.46996239, 3.08241149], '
                                               '[23.8912344, 10.9982611, 5.84966811]])\n'
                                               '>>> np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> linear = Linear_41(2, 3)\n'
                                               '>>> _ = linear.forward(X_sss)\n'
                                               '>>> dLdZ = np.array([[1, 1, 0, 0], [2, 0, 1, 0], [3, 0, 0, 1]]).T\n'
                                               '>>> dLdA = linear.backward(dLdZ)\n'
                                               '>>> expected = np.array([[3.88949792, 2.15255717], [1.24737338, 1.58455078], [0.28295388, 1.32056292], [0.69207227, -0.69103982]])\n'
                                               '>>> np.allclose(dLdA, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> linear = Linear_41(2, 3)\n'
                                               '>>> _ = linear.forward(X_sss)\n'
                                               '>>> dLdZ = np.array([[1, 1, 0, 0], [2, 0, 1, 0], [3, 0, 0, 1]]).T\n'
                                               '>>> _ = linear.backward(dLdZ)\n'
                                               '>>> ans = linear.dLdW\n'
                                               '>>> expected = np.array([[5, 13, 18], [7, 16, 20]])\n'
                                               '>>> np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> linear = Linear_41(2, 3)\n'
                                               '>>> _ = linear.forward(X_sss)\n'
                                               '>>> dLdZ = np.array([[1, 1, 0, 0], [2, 0, 1, 0], [3, 0, 0, 1]]).T\n'
                                               '>>> _ = linear.backward(dLdZ)\n'
                                               '>>> ans = linear.dLdW0\n'
                                               '>>> expected = np.array([[2, 3, 4]])\n'
                                               '>>> np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> linear = Linear_41(2, 3)\n'
                                               '>>> _ = linear.forward(X_sss)\n'
                                               '>>> dLdZ = np.array([[1, 1, 0, 0], [2, 0, 1, 0], [3, 0, 0, 1]]).T\n'
                                               '>>> _ = linear.backward(dLdZ)\n'
                                               '>>> linear.sgd_step(0.005)\n'
                                               '>>> ans = np.vstack([linear.W, linear.W0])\n'
                                               '>>> expected = np.array([[1.22237338, 0.21795388, 0.60207227], [1.54955078, 1.24056292, -0.79103982], [-0.01, -0.015, -0.02]])\n'
                                               '>>> np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
