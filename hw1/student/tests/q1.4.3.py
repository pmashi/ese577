OK_FORMAT = True

test = {   'name': 'q1.4.3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> col_v = np.array([[1], [2], [3]])\n>>> isinstance(length_143(col_v), (float, np.number))\nTrue',
                                       'failure_message': 'Your function does not return a scalar float.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> col_v = np.array([[1], [2], [3]])\n>>> np.isclose(length_143(col_v), np.sqrt(14)).item()\nTrue',
                                       'failure_message': 'Your function does not return the correct float.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> import inspect\n'
                                               '>>> length_143_str = inspect.getsource(length_143)\n'
                                               ">>> 'for' not in length_143_str and 'while' not in length_143_str and ('linalg' not in length_143_str)\n"
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
