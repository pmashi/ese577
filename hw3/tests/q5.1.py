OK_FORMAT = True

test = {   'name': 'q5.1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(ans_51, list) and len(ans_51) == 3 and all((isinstance(x, (float, int, np.number)) for x in ans_51))\nTrue',
                                       'failure_message': 'Answer is not a 3-list of scalars.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {'code': '>>> all((x >= 0 for x in ans_51)) and np.isclose(sum(ans_51), 1, rtol=0.02).item()\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
