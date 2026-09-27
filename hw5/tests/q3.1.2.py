OK_FORMAT = True

test = {   'name': 'q3.1.2',
    'points': 7,
    'suites': [   {   'cases': [   {   'code': '>>> A = np.array([[1, 2, 3]])\n'
                                               '>>> Z = np.array([[1, 2]])\n'
                                               '>>> dLdZ = np.array([[1, 2]])\n'
                                               '>>> W = np.array([[1, 2], [3, 4], [5, 6]])\n'
                                               '>>> W_0 = np.array([[1, 2]])\n'
                                               '>>> isinstance(dLdW_312(A, Z, dLdZ, W, W_0), np.ndarray) and dLdW_312(A, Z, dLdZ, W, W_0).shape == (3, 2)\n'
                                               'True',
                                       'failure_message': 'Does not return a m x n numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
