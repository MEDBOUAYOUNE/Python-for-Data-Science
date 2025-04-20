import sys

def words_greater_than_n():
    new_list = []
    n = 0
    string = None
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"

        if int(sys.argv[2]):
            n = int(sys.argv[2])
        string = sys.argv[1]

        check_lambda = lambda word: len(word) > n 

        new_list = [word for word in string.split() if check_lambda(word)]

        # for word in string.split():
        #     if len(word) > n:
        #         new_list.append(word)
        
        print(new_list)
        
    except AssertionError as error:
        print(error)
    except ValueError as e:
        print(new_list)


if __name__ == "__main__":
    words_greater_than_n()