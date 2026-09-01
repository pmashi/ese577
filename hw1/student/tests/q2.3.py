OK_FORMAT = True

test = {   'name': 'q2.3',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> X = np.array([[1, 2], [3, 4], [1, 3]])\n'
                                               '>>> th = np.array([[0.5], [1.0]])\n'
                                               '>>> th0 = 0.1\n'
                                               '>>> isinstance(lin_reg_predict_23(X, th, th0), np.ndarray)\n'
                                               'True',
                                       'failure_message': 'Your function does not return a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X = np.array([[1, 2], [3, 4], [1, 3]])\n>>> th = np.array([[0.5], [1.0]])\n>>> th0 = 0.1\n>>> lin_reg_predict_23(X, th, th0).shape == (3, 1)\nTrue',
                                       'failure_message': 'Your function does not return a column vector of the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X = np.array([[1, 2], [3, 4], [1, 3]])\n'
                                               '>>> th = np.array([[0.5], [1.0]])\n'
                                               '>>> th0 = 0.1\n'
                                               '>>> np.allclose(lin_reg_predict_23(X, th, th0), np.array([[2.6], [5.6], [3.6]]))\n'
                                               'True',
                                       'failure_message': 'Your function does not return the correct column vector.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> lin_reg_predict_23_str = inspect.getsource(lin_reg_predict_23)\n'
                                               ">>> 'for' not in lin_reg_predict_23_str and 'while' not in lin_reg_predict_23_str\n"
                                               'True',
                                       'failure_message': "Your function contains a loop. Please remove all for/while loops. (If have comments containing the words 'for' or 'while', please remove "
                                                          'those comments as well.)',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
