OK_FORMAT = True

test = {   'name': 'q3.2',
    'points': 25,
    'suites': [   {   'cases': [   {   'code': '>>> states = [0, 1, 2, 3]\n'
                                               ">>> actions = ['b', 'c']\n"
                                               '>>> def transition_fn(s, a):\n'
                                               '...     if s == 0:\n'
                                               "...         if a == 'b':\n"
                                               '...             return DDist({0: 0.0, 1: 0.9, 2: 0.1, 3: 0.0})\n'
                                               "...         elif a == 'c':\n"
                                               '...             return DDist({0: 0.0, 1: 0.1, 2: 0.9, 3: 0.0})\n'
                                               '...     elif s == 1:\n'
                                               '...         return DDist({0: 0.9, 1: 0.1, 2: 0.0, 3: 0.0})\n'
                                               '...     elif s == 2:\n'
                                               '...         return DDist({0: 0.0, 1: 0.0, 2: 0.1, 3: 0.9})\n'
                                               '...     elif s == 3:\n'
                                               '...         return DDist({0: 0.9, 1: 0.0, 2: 0.0, 3: 0.1})\n'
                                               '>>> def reward_fn(s, a):\n'
                                               '...     if s == 1:\n'
                                               '...         return 1\n'
                                               '...     elif s == 3:\n'
                                               '...         return 2\n'
                                               '...     else:\n'
                                               '...         return 0\n'
                                               '>>> mdp = MDP(states, actions, transition_fn, reward_fn, discount_factor=0.9)\n'
                                               ">>> q = TabularQ([0, 1, 2, 3], ['b', 'c'])\n"
                                               '>>> learned_q = value_iteration_32(mdp, q)\n'
                                               ">>> learned_q.get(0, 'b') < learned_q.get(0, 'c') and learned_q.get(1, 'b') == learned_q.get(1, 'c') and (learned_q.get(2, 'b') == learned_q.get(2, "
                                               "'c')) and (learned_q.get(3, 'b') == learned_q.get(3, 'c'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
