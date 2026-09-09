OK_FORMAT = True

test = {   'name': 'q1.2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> theta_1 = 0.1\n>>> theta_2 = 0.2\n>>> isinstance(grad_12(theta_1, theta_2), (float, np.number))\nTrue',
                                       'failure_message': 'Did not return a scalar float.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> theta_1 = 0.1\n>>> theta_2 = 0.2\n>>> np.isclose(grad_12(theta_1, theta_2), 2.3).item()\nTrue',
                                       'failure_message': 'Did not return the correct value.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
