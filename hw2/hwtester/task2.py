def test(fnc):
    test_input = """
        the history of clocks begins with ancient civilizations using sundials to track time by observing the position of the sun the earliest known sundials date back to ancient egypt around 1500 bce as timekeeping devices became more sophisticated mechanical clocks emerged in medieval europe by the 13th century these early mechanical clocks were large and used primarily in churches to mark the hours the invention of the pendulum in the 17th century greatly improved accuracy leading to more precise timekeeping devices in the 18th and 19th centuries clocks became smaller and more accessible with the development of the balance spring and the quartz crystal the 20th century saw the rise of electronic clocks and digital displays making timekeeping even more accurate and convenient
    """
    
    test1_output = ['using', 'track', 'known', 'egypt', 'these', 'early', 'large', 'hours']

    test2_output = ['of',
 'to',
 'by',
 'of',
 'to',
 'as',
 'in',
 'by',
 'in',
 'to',
 'of',
 'in',
 'to',
 'in',
 'of',
 'of']

    test3_output = ['clocks',
 'begins',
 'around',
 'became',
 'clocks',
 'europe',
 'clocks',
 'clocks',
 'became',
 'spring',
 'quartz',
 'clocks',
 'making']
    
    test4_output = ['observing', 'primarily', 'invention', 'centuries']


    test5_output = ['timekeeping', 'timekeeping', 'development', 'timekeeping']

    
    if fnc.__name__ == "find_len5_words":
        if fnc(test_input) == test1_output:
            print("task2.1 [PASS]")
        else:
            print("task2.1 [NOT pass]")

    elif fnc.__name__ == "find_words":  
        for n, t in [(2,  test2_output), 
                     (5,  test3_output), 
                     (9,  test4_output), 
                     (11, test5_output)]:
            if fnc(test_input, n) == t:
                print(f"task2.2 ({n}) [pass]")
            else:
                print(f"task2.2 ({n}) [NOT pass]")
    