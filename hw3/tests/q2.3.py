OK_FORMAT = True

test = {   'name': 'q2.3',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> theta_0 = np.array(0.4)\n>>> theta = np.array(0.5)\n>>> isinstance(separator_23(theta, theta_0), (float, int, np.number))\nTrue',
                                       'failure_message': 'Did not return a scalar.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> theta_0 = np.array(0.4)\n>>> theta = np.array(0.5)\n>>> np.isclose(separator_23(theta, theta_0), -0.8).item()\nTrue',
                                       'failure_message': 'Did not return the correct value.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
