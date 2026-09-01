OK_FORMAT = True

test = {   'name': 'q2.2',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> x = np.array([[1], [3]])\n'
                                               '>>> th = np.array([[0.5], [1.0]])\n'
                                               '>>> th0 = 0.1\n'
                                               '>>> isinstance(lin_reg_predict_single_22(x, th, th0), np.ndarray)\n'
                                               'True',
                                       'failure_message': 'Your function does not return a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> x = np.array([[1], [3]])\n>>> th = np.array([[0.5], [1.0]])\n>>> th0 = 0.1\n>>> lin_reg_predict_single_22(x, th, th0).shape == (1, 1)\nTrue',
                                       'failure_message': 'Your function does not return a 1x1 numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> x = np.array([[1], [3]])\n'
                                               '>>> th = np.array([[0.5], [1.0]])\n'
                                               '>>> th0 = 0.1\n'
                                               '>>> np.allclose(lin_reg_predict_single_22(x, th, th0), np.array([[3.6]]))\n'
                                               'True',
                                       'failure_message': 'Your function does not return the correct value.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
