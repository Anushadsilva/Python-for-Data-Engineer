
import json_prac

def sum(x,y):
    return x + y


def sum_args(*args):
    tot = 0
    for i in args:
        tot += i
    return tot

def concate_string(**kwargs):
    ans = ""
    for k,v in kwargs.items():
        print(f'key: {k}, value: {v}')
        ans += v + " "
    return ans


if __name__ == '__main__':
    print("Hi")
    x = 4
    y = 2

    print('sum', x+y)
    print('mod' , x % y)
    print('div' , x / y)
    print('mod', x//y)
    print('div', x % y)

    print("Hello" + "World")
    s= "HI"
    print(s[0])
    print(str(5))

    s= "Hello"
    print(s.lower())
    print(s.upper())
    print(s.capitalize())
    print(s.title())
    print(s.count('o'))
    print(s.find('o'))
    print(s.index('o'))
    print(s.rfind('o'))
    print(s.rindex('o'))
    assert s.isalpha()
    assert s.isalnum()

    s= str(123)
    assert s.isnumeric()

    s= "10.3.#.5.4#5.6"

    split = s.split("#")
    print(split)
    join_str = "*".join(split)
    print(join_str)
    repl = join_str.replace("*", "#")
    print(repl)
    print(len(repl))

    s= False
    print(f'typeof s: {type(s)}, id of s : {id(s)}')

    #Loop
    x= "python"
    for i in x:
        print(i)

    x = ["1","hello","no"]
    for i in x:
        print(i)

    i =1
    while (i < 5):
        print(i)
        i = i + 1
        if i % 2 == 0:
            continue
        else:
            break


    print(f'2 sum: {sum(1,2)}')
    print(f'sum of number: {sum_args(1,2,3,4,5)}')
    print(concate_string(one='python', two='is', three='fun'))


    carrers = ['ml','de','cs','la']

    for idx ,carrer in enumerate(carrers):
        print(f'{idx}: {carrer}')

    print(carrers[0],carrers[-1])
    print(carrers[::-1])
    print(carrers[1:])
    print(carrers[:2])
    print(carrers[-3:])

json_str = """{
    "Python" :"Learning Python",
    "age" : 30,
    "city" :"USA"
}"""

data = json.loads(json_str)
print(type(data))
print(data)

dp = {
    "Python" :"Learning Python",
    "age" : 30,
    "city" :"USA"
}

data = json.dumps(dp)
print(type(data))
print(data)
