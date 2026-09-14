OK_FORMAT = True

test = {   'name': 'q4.6',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> g = np.array([[0.5]])\n'
                                               '>>> y = np.array([[1]])\n'
                                               '>>> x = np.array([[0.5], [0.6]])\n'
                                               '>>> isinstance(grad_loss_46(x, y, g), np.ndarray) and grad_loss_46(x, y, g).shape == (2, 1)\n'
                                               'True',
                                       'failure_message': 'Did not return a numpy array of the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> g = np.array([[0.5]])\n'
                                               '>>> y = np.array([[1]])\n'
                                               '>>> x = np.array([[0.5], [0.6]])\n'
                                               '>>> np.allclose(grad_loss_46(x, y, g), np.array([[-0.25], [-0.3]]))\n'
                                               'True',
                                       'failure_message': 'Did not return the correct gradient.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
