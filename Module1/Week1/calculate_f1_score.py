def calc_f1_score(tp, fp, fn):
    assert type(tp) == int, "tp must be int"
    assert type(fp) == int, "fp must be int"
    assert type(fn) == int, "fn must be int"
    assert tp > 0 and fp > 0 and fn > 0, "tp and fp and fn must be greater than zero"

    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2 * (precision*recall)/(precision+recall)

    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1-score is {f1_score}")
