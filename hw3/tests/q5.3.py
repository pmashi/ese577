OK_FORMAT = True

test = {   'name': 'q5.3',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(ans_53, list) and all((isinstance(x, list) for x in ans_53)) and all((isinstance(x, (float, int, np.number)) for sublist in ans_53 for '
                                               'x in sublist))\n'
                                               'True',
                                       'failure_message': 'Answer is not a list of lists.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
