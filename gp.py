import random

def gen_rnd_expr(func_set, term_set, max_d, method):
    n_term_set = len(term_set)
    n_func_set = len(func_set)
    p = n_term_set / (n_term_set + n_func_set)
    if max_d == False or (method == 'grow' and random.random() < p):
        expr = random.choice(term_set)
    else:
        func = random.choice(func_set) 
        args = []
        for i in range(2):
            arg_i = random.choice(func_set, term_set, max_d - 1, method)
            args.append(arg_i)
        expr = func(args[0], args[1])
    return expr


def evaluate(expr):
    if isinstance(expr, list):
        proc = expr[0] ## non-terminal, extract root
        IsFunc = str(type(proc)) == "<class 'function'>"
        if IsFunc:
            value = proc(evaluate(expr[1]), evaluate(expr[2])) ## function, evaluate args
        else:
            value = proc(expr[1], expr[2]) ## macro, don't evaluate args
    else:
        IsNotFunc = str(type(proc)) != "<class 'function'>"
        if IsNotFunc:
            value = expr
        else:
            value = expr() ## terminal 0-arity function
    return value
