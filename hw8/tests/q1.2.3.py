OK_FORMAT = True

test = {   'name': 'q1.2.3',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(v_123, list) and len(v_123) == 4 and all((isinstance(x, (int, float, np.number)) for x in v_123))\nTrue',
                                       'failure_message': 'Did not return a 4-list of scalars.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
