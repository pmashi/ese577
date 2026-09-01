OK_FORMAT = True

test = {   'name': 'q1.4.5',
    'points': 0.5,
    'suites': [   {   'cases': [   {   'code': '>>> A = np.array([[1, 2, 3], [4, 5, 6]])\n>>> isinstance(index_final_col_145(A), np.ndarray)\nTrue',
                                       'failure_message': 'Your function does not return a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> A = np.array([[1, 2, 3], [4, 5, 6]])\n>>> index_final_col_145(A).shape == (2, 1)\nTrue',
                                       'failure_message': 'Your function does not return a column vector of the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> A = np.array([[1, 2, 3], [4, 5, 6]])\n>>> np.allclose(index_final_col_145(A), np.array([[3], [6]]))\nTrue',
                                       'failure_message': 'Your function does not return the final column.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> import inspect\n'
                                               '>>> index_final_col_145_str = inspect.getsource(index_final_col_145)\n'
                                               ">>> 'for' not in index_final_col_145_str and 'while' not in index_final_col_145_str\n"
                                               'True',
                                       'failure_message': "Your function contains a loop. Please remove all for/while loops. (If have comments containing the words 'for' or 'while', or 'linalg'.)",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
