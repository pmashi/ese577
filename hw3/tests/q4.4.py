OK_FORMAT = True

test = {   'name': 'q4.4',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> g = np.array([[0.4]])\n'
                                               '>>> x = np.array([[0.5], [0.6]])\n'
                                               '>>> isinstance(grad_sigmoid_44(g, x), np.ndarray) and grad_sigmoid_44(g, x).shape == (2, 1)\n'
                                               'True',
                                       'failure_message': 'Does not return a numpy array of the right shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
