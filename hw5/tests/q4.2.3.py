OK_FORMAT = True

test = {   'name': 'q4.2.3',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> softmax = SoftMax_423()\n'
                                               '>>> ans = softmax.forward(X_sss)\n'
                                               '>>> expected = np.array([[0.04742587317756679, 0.7310585786300048, 0.9525741268224334, 0.9990889488055993], [0.9525741268224333, 0.2689414213699951, '
                                               '0.04742587317756678, 0.0009110511944006454]]).T\n'
                                               '>>> np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> softmax = SoftMax_423()\n'
                                               '>>> ans = softmax.class_fun(y_sss)\n'
                                               '>>> expected = np.array([1, 0, 1, 0])\n'
                                               '>>> np.allclose(ans, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
