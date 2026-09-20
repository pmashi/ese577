OK_FORMAT = True

test = {   'name': 'q4.3',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': ">>> isinstance(data_42, list) and all((isinstance(x, tuple) and len(x) == 2 and (x[0] in ('sr', 'sg', 'sb', 'mr', 'mg', 'mb', 'lr', 'lg', 'lb')) and "
                                               'isinstance(x[1], int) for x in data_42)) or data_42 is None\n'
                                               'True',
                                       'failure_message': 'Answer is not a list of 2-tuples with a string and an int, or None.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> len(data_43) == len(set((x[0] for x in data_43))) if data_43 is not None else True\nTrue',
                                       'failure_message': 'Answer contains repeated inputs.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
