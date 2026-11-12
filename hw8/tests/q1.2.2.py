OK_FORMAT = True

test = {   'name': 'q1.2.2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(C_122, list) and len(C_122) == 4 and all((isinstance(row, list) and len(row) == 4 and all((isinstance(x, (int, float, np.number)) for x '
                                               'in row)) for row in C_122))\n'
                                               'True',
                                       'failure_message': 'Answer is not a 4-list of 4-lists of scalars.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
