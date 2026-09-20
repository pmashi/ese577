OK_FORMAT = True

test = {   'name': 'q2.5',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(ans_25, list) and all((isinstance(row, list) for row in ans_25)) and (len(ans_25) == 2) and all((len(row) == 2 for row in ans_25)) or '
                                               'ans_25 is None\n'
                                               'True',
                                       'failure_message': 'Answer is not a 2-list of 2-lists or None.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
