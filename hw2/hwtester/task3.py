def test(d_or_fnc):
    from inspect import isfunction
    import io
    
    if type(d_or_fnc) is dict:
        test_output = [(2, 'i'),
             (13, 'of'),
             (25, 'all'),
             (64, 'have'),
             (59, 'small'),
             (27, 'unique'),
             (32, 'borders'),
             (18, 'possible'),
             (19, 'legendary'),
             (11, 'invitation'),
             (2, 'performance'),
             (2, 'preservation'),
             (3, 'sensibilities')]

        for i in range(1, 14):   
            try:
                if len(d_or_fnc[i]) == test_output[i-1][0] and test_output[i-1][1] in set(d_or_fnc[i]):
                    print(f"test3.1 ({i}) [PASS]")
                else:
                    print(f"test3.1 ({i}) [NOT pass]")
                    print(i, test_output, d_or_fnc[i])
            except:
                print(f"test3.1 ({i}) [not PASS]")

    elif isfunction(d_or_fnc):
        if d_or_fnc.__name__ == "generate_sentence":
            w_map = {
             2: ['of', 'in', 'by', 'to', 'as'],
             3: ['the', 'sun', 'bce', 'and', 'saw'],
             4: ['mark',
              'more',
              '13th',
              'used',
              '20th',
              'rise',
              'back',
              'time',
              'with',
              'date',
              '17th',
              '18th',
              '19th',
              'were',
              'even',
              '1500'],
             5: ['track', 'egypt', 'hours', 'these', 'using', 'large', 'known', 'early'],
             6: ['begins',
              'around',
              'quartz',
              'spring',
              'clocks',
              'became',
              'europe',
              'making'],
             7: ['devices',
              'crystal',
              'ancient',
              'greatly',
              'emerged',
              'century',
              'balance',
              'history',
              'smaller',
              'digital',
              'precise',
              'leading'],
             8: ['displays',
              'position',
              'accuracy',
              'accurate',
              'earliest',
              'pendulum',
              'churches',
              'improved',
              'medieval',
              'sundials'],
             9: ['centuries', 'primarily', 'invention', 'observing'],
             10: ['electronic', 'accessible', 'convenient', 'mechanical'],
             11: ['timekeeping', 'development'],
             13: ['sophisticated', 'civilizations']
            }

            
            test_input = [
                [3, 6, 3, 5, 4, 9],
                [3, 3, 6, 5, 3, 4],
                [4, 4, 8, 4, 2, 5],
                [4, 4, 7, 4, 2, 3],
                [4, 8, 4, 4, 1, 6]
            ]

            for t in test_input:
                try:
                    s = d_or_fnc(t, w_map).split()
                    
                    if [len(w) for w in s] == t and \
                       all([w in w_map[len(w)] for w in s]):
                        print("[PASS]")
                    else:
                        print([w in w_map[len(w)] for w in s])
                        print("[not PASS]")
                except:
                    print("[not PASS]")
                    
    elif isinstance(d_or_fnc, io.IOBase):
        sentence_template =  [
          [1, 5, 2, 7, 2, 8],
          [3, 6, 3, 5, 4, 9],
          [3, 3, 6, 5, 3, 4],
          [4, 4, 8, 4, 2, 5],
          [4, 8, 4, 4, 1, 6]
        ]
        for s in sentence_template:
            try:
                for l in d_or_fnc:
                    if [len(w) for w in l.split()] == s:
                        print("[PASS]")
                    else:
                        print("[not PASS]")
                else:
                    print("[not PASS]")

            except:
                print("[not PASS]")