OK_FORMAT = True

test = {   'name': 'q1.4.4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> col_v = np.array([[1], [2], [3]])\n>>> isinstance(normalize_144(col_v), np.ndarray)\nTrue',
                                       'failure_message': 'Your function does not return a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> col_v = np.array([[1], [2], [3]])\n>>> normalize_144(col_v).shape == col_v.shape\nTrue',
                                       'failure_message': 'Your function does not return a numpy array of the same shape as the original array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> col_v = np.array([[1], [2], [3]])\n>>> np.isclose(length_143(normalize_144(col_v)), 1).item()\nTrue',
                                       'failure_message': 'Your function does not return an array of length 1, according to your own function length_143.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> import inspect\n'
                                               '>>> normalize_144_str = inspect.getsource(normalize_144)\n'
                                               ">>> 'for' not in normalize_144_str and 'while' not in normalize_144_str and ('linalg' not in normalize_144_str)\n"
                                               'True',
                                       'failure_message': 'Your function contains a loop or a call to np.linalg. Please remove all for/while loops and calls to np.linalg. (If have comments '
                                                          "containing the words 'for', 'while', or 'linalg', please remove those comments as well.)",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
