OK_FORMAT = True

test = {   'name': 'q3.3',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(filters_33, list) and len(filters_33) == 4 and all((isinstance(x, list) and len(x) == 2 and all((isinstance(y, list) and len(y) == 2 '
                                               'and all((isinstance(z, int) and z in [-1, 1] for z in y)) for y in x)) for x in filters_33))\n'
                                               'True',
                                       'failure_message': "Answer is not an 4-list of 2-lists of 2-lists of -1/+1's.",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
