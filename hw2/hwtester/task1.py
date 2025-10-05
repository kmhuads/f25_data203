def test(fnc):
    if fnc.__name__ == "find_largest_prime":    
        with open("data/test_data.txt") as f:
            data = [l.strip() for l in f.readlines()]
            
            for i, d in enumerate(data):
                output = d.split(",")[0] 
                output = None if output == "None" else int(output)
                inputs = [int(n) for n in d.split(",")[1:]]
    
                print(f"[Test {i}] -> ", end="")
    
                fnc_output = fnc(inputs)
                if fnc_output == output:
                    print("task 1.1 [PASS]")
                else:
                    print("task 1.1 [NOT pass]")
                    print("\n\tinput: ", inputs)
                    print("\n\tEXPECTED output: ", output)
                    print("\tYOUR     output: ", fnc_output)
                    print()