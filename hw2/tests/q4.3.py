OK_FORMAT = True

test = {   'name': 'q4.3',
    'points': 7.5,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(thetas_43, list) and len(thetas_43) == 4\nTrue',
                                       'failure_message': 'Answer is not a 4-element list.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> all((isinstance(t, (float, int, np.number)) for t in thetas_43))\nTrue',
                                       'failure_message': 'Elements of the list are not scalar floats.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
