OK_FORMAT = True

test = {   'name': 'q2.4',
    'points': 4.5,
    'suites': [   {   'cases': [   {   'code': '>>> x = np.array([[1], [2]])\n'
                                               '>>> theta = np.array([[0.1], [0.2]])\n'
                                               '>>> y = np.array([[0.5]])\n'
                                               '>>> isinstance(grad_huber_24(x, y, theta), np.ndarray)\n'
                                               'True',
                                       'failure_message': 'Did not return a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> x = np.array([[1], [2]])\n>>> theta = np.array([[0.1], [0.2]])\n>>> y = np.array([[0.5]])\n>>> grad_huber_24(x, y, theta).shape == (2, 1)\nTrue',
                                       'failure_message': 'Did not return a d x 1 array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> x = np.array([[1], [2]])\n'
                                               '>>> theta = np.array([[0.1], [0.2]])\n'
                                               '>>> y = np.array([[0.5]])\n'
                                               '>>> np.allclose(grad_huber_24(x, y, theta), np.zeros((2, 1)))\n'
                                               'True',
                                       'failure_message': 'Did not return the correct value.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
