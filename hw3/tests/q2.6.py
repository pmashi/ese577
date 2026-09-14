OK_FORMAT = True

test = {   'name': 'q2.6',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> theta = 0.5\n'
                                               '>>> theta_0 = 0.4\n'
                                               '>>> isinstance(parameters_26(theta, theta_0), tuple) and len(parameters_26(theta, theta_0)) == 2 and all((isinstance(x, (float, int, np.number)) for x '
                                               'in parameters_26(theta, theta_0)))\n'
                                               'True',
                                       'failure_message': 'Did not return a 2-tuple of scalars.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> theta = 0.5\n'
                                               '>>> theta_0 = 0.4\n'
                                               '>>> theta_new, theta_0_new = parameters_26(theta, theta_0)\n'
                                               '>>> np.isclose(theta_new, 0.5).item() and np.isclose(theta_0_new, -0.1).item()\n'
                                               'True',
                                       'failure_message': 'Did not return the correct values.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
