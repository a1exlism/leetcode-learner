""" SORT
    @refer: https://docs.python.org/zh-cn/3.6/howto/sorting.html
"""
import operator
if __name__ == "__main__":
    """ sort list """
    l = list('679341465432')
    sorted_l = sorted(l)
    print(f'list: {l} \nsorted list: {sorted_l}')
    # l.sort()  # replace origin list
    # print(f'sorted list: {l}')
    sorted_r_l = sorted(l, reverse=True)
    print(f'list: {l} \nsorted reversed list: {sorted_r_l}')

    """ sort dict
        @refer: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    """
    d = {
        345: [22, 45],
        13: [64, 11],
        1113: [54, 11],
        5: [6411, 11],
        12: [222, 133],
    }
    sorted_d = sorted(d.items(), key=operator.itemgetter(1),
                      reverse=True)  # small -> large
    print(f'dict: {d} \nsorted dict: {sorted_d}')
