class Evaluator:
    def zip_evaluate(coefs, words):
        result = 0
        if isinstance(words, list) and isinstance(coefs, list):
            if len(words) == len(coefs):
                for one, two in zip(words, coefs):
                    result += len(one) * two
                print(result)
            else:
                print(-1)
        else:
            print(-1)

    def enumerate_evaluate(coefs, words):
        result = 0
        if isinstance(words, list) and isinstance(coefs, list):
            if len(words) == len(coefs):
                for i, one in enumerate(words):
                    result += len(one) * coefs[i]
                print(result)
            else:
                print(-1)
        else:
            print(-1)
