OK_FORMAT = True

test = {   'name': 'q5.2.2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(ans_522, list) and all((isinstance(x, list) for x in ans_522)) and all((isinstance(x, (float, int, np.number)) for sublist in ans_522 '
                                               'for x in sublist))\n'
                                               'True',
                                       'failure_message': 'Answer is not a list of lists.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
