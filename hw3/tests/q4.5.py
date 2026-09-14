OK_FORMAT = True

test = {   'name': 'q4.5',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> g = 0.5\n>>> y = 1\n>>> isinstance(dloss_dg_45(g, y), (float, np.number))\nTrue',
                                       'failure_message': 'Did not return a scalar.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> g = 0.5\n>>> y = 1\n>>> dloss_dg_45(g, y) == -2\nTrue',
                                       'failure_message': 'Did not return the correct value.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
