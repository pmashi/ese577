OK_FORMAT = True

test = {   'name': 'q2.3',
    'points': 4.5,
    'suites': [   {   'cases': [   {   'code': '>>> g = 0.5\n>>> a = 0.5\n>>> isinstance(derivative_huber_23(g, a), (float, np.number))\nTrue',
                                       'failure_message': 'Did not return a scalar float.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> g = 0.5\n>>> a = 0.5\n>>> np.isclose(derivative_huber_23(g, a), 0.0).item()\nTrue',
                                       'failure_message': 'Did not return the correct value.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
