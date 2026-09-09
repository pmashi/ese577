OK_FORMAT = True

test = {   'name': 'q4.2',
    'points': 7.5,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(thetas_42, list) and len(thetas_42) == 2\nTrue',
                                       'failure_message': 'Answer is not a 2-element list.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> all((isinstance(t, (float, int, np.number)) for t in thetas_42))\nTrue',
                                       'failure_message': 'The elements of the list are not scalar floats.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
