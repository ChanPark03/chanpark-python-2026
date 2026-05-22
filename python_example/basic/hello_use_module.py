from a35_variable_length_keyward_argument import print_n_times as pnt
from test_package.module_a import module_var_a
from test_package.module_b import module_var_b


def main():
    print("hello world")
    print(__name__)
    pnt(1,2,3, b="bbb")
    
    print(module_var_a)
    print( module_var_b)
#import 를 당했을때 __main__이 아니라 hello가 출력된다.
if __name__ == "__main__":
    main()