from z3 import *
import click

import sys
import re


@click.command()
@click.option("--input", "-i", required=True, help="The input file of the sat problem")
@click.option("--input_prefix", "-p", default="P", help="The prefix of all input states")
@click.option("--all", "-a", is_flag=True, default=False, help="Whether all satisfiable inputs should be listed")
@click.option("--string", "-s", is_flag=True, default=False, help="Convert all input states to a binary string")
def solve(input, input_prefix, all, string):
    # get input, strip empty lines and extra whitspace
    f = open(input)
    lines = [x for x in [x.strip() for x in f.readlines()] if len(x) > 0 and x[0] != "#"]

    # converts all multiple whitespace to a single space and splits up terms
    lines = [re.sub(r"\s+", " ", x).split(" ") for x in lines]

    solver = Solver()

    inputs = []

    def parse_term(term):
        stripped = term.replace("~", "")
        x = Bool(stripped)
        if stripped.startswith(input_prefix) and x not in inputs:
            inputs.append(x)
        return Not(x) if term[0] == "~" else x

    def print_term(term, term_str):
        if string:
            print(1 if term else 0, end="")
        else:
            print(term_str if term else "~" + term_str, end=" ")

    for line in lines:
        solver.add(Or([parse_term(term) for term in line]))

    while solver.check() == sat:
        duplicate_check = []
        for i in list(inputs):
            print_term(solver.model()[i], str(i))
            duplicate_check.append(i != solver.model()[i])
        solver.add(Or(duplicate_check))
        print()
        if not all:
            exit()


if __name__ == "__main__":
    solve()
