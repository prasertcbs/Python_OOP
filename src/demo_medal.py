# from medal import Medal, Athlete, Foo
# import medal

import medal as md

if __name__ == '__main__':
    th = md.Medal("Thailand", 3, 4, 5)
    print(th.total())

    a = md.Athlete()
