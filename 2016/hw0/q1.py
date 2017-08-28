import sys
import os.path

def solve_q1(col_idx, dat_name):
    """
    Don't expect input form, naively read file
    sort by their value, but output with the original form (e.g. "+1")
    """
    with open(dat_name, 'r') as f:
        col_data = [line.strip().split(' ')[col_idx] for line in f]
    col_val = map(eval, col_data)
#     print col_val[:5]
    sorted_val, sorted_data = zip(*sorted(zip(col_val, col_data)))
#     print sorted_val[:5]
#     print sorted_data[:5]
    with open('ans1.txt', 'wb') as f:
        f.write(','.join(sorted_data))

if __name__ == "__main__":
    try:
        col_idx = int(sys.argv[1])
        dat_name = sys.argv[2]
    except:
        print "invalid input argv: {a}".format(a=sys.argv)
        raise
    assert os.path.isfile(dat_name)
    
    solve_q1(col_idx, dat_name)
    