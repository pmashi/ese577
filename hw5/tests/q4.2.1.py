OK_FORMAT = True

test = {   'name': 'q4.2.1',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> tanh = Tanh_421()\n'
                                               '>>> ans = tanh.forward(X_sss)\n'
                                               '>>> expected = np.array([[0.96402758, 0.9999092], [0.99505475, 0.96402758], [0.99999997, 0.99998771], [1.0, 0.9999092]])\n'
                                               '>>> np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> tanh = Tanh_421()\n'
                                               '>>> _ = tanh.forward(X_sss)\n'
                                               '>>> dLdA = np.array([[1, 1, 0, 0], [2, 0, 1, 0]]).T\n'
                                               '>>> ans = tanh.backward(dLdA)\n'
                                               '>>> expected = np.array([[0.07065082485316443, 0.009866037165440211, 0.0, 0.0], [0.0003631664618877206, 0.0, 2.4576547405286142e-05, 0.0]]).T\n'
                                               '>>> np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
