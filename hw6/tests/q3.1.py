OK_FORMAT = True

test = {   'name': 'q3.1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(ans_31, list) and len(ans_31) == 2 and isinstance(ans_31[0], list) and all((isinstance(x, int) for x in ans_31[0])) and (len(ans_31[0]) '
                                               '== 2) and isinstance(ans_31[1], int)\n'
                                               'True',
                                       'failure_message': 'Answer is not a 2-list with a 2-list of integers and a scalar integer.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
