#!/usr/bin/env python3
import itertools


def dfa2sat(E: list[tuple[int, int, str]], q: int, F: list[int]):
    """
    Convert DFA to SAT.

    Arguments:
    - E: list of edges (source, target, label)
    - q: starting state
    - F: list of final states
    """
    min_node = min(min(e[0], e[1]) for e in E)
    max_node = max(max(e[0], e[1]) for e in E)

    print("# At least one state in each step.")
    for i in range(len(E)):
        qs = [f"Q{j}_{i}" for j in range(max_node - min_node + 1)]
        print(" ".join(qs))

    for i in range(len(E)):
        print()
        print(f"# No more than one state at step {i}.")
        for j in itertools.combinations(range(max_node - min_node + 1), 2):
            print(f"~Q{j[0]}_{i} ~Q{j[1]}_{i}")

    for i in range(len(E)):
        src = E[i][0]
        dst = E[i][1]
        trans = E[i][2]
        print()
        print(f"# Transition at step {i} ({src} ─{trans}🡪 {dst}).")
        for j in range(len(E) - 1):
            p = "~" if trans == "1" else ""
            print(f"~Q{src}_{j} {p}P{j} Q{dst}_{j+1}")

    print()
    print("# Initial state.")
    print(f"Q{q}_{0}")

    print()
    print("# Final state(s).")
    for f in F:
        end = [f"Q{f}_{i}" for i in range(len(E))]
        print(" ".join(end))


dfa2sat(
    [
        (0, 1, "1"),
        (0, 0, "0"),
        (1, 2, "1"),
        (1, 0, "0"),
        (2, 3, "0"),
        (2, 0, "1"),
    ],
    0,
    [3],
)
