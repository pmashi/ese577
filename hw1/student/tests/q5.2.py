OK_FORMAT = True

test = {   'name': 'q5.2',
    'points': 10,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(errors_52, list)\nTrue', 'failure_message': 'Your answer is not a list.', 'hidden': False, 'locked': False, 'points': 0},
                                   {   'code': '>>> len(errors_52) == 4 and all((isinstance(err, (int, float, np.number)) for err in errors_52))\nTrue',
                                       'failure_message': 'Your answer is not a 4-list of scalars.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
