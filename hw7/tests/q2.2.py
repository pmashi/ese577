OK_FORMAT = True

test = {   'name': 'q2.2',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(W_right_22, list) and len(W_right_22) == 2 and all((isinstance(row, list) and len(row) == 2 and all((isinstance(x, (int, float, '
                                               'np.number)) for x in row)) for row in W_right_22))\n'
                                               'True',
                                       'failure_message': 'Answer is not a 2-list of 2-lists of scalars.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
