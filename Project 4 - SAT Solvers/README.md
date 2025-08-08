# Python SAT Solver using Z3

## Installation

```bash
python -m pip install -r requirements.txt
```

## Usage

To get a list of options
```
python main.py --help
```

Uses the `inputs/substring.in` regular language, prints all possible outputs, represents states as a binary string
```
python main.py --input inputs/substring.in --all --string
```

### Input Format

The input file is expected to be in conjunctive normal form (CNF). CNF is a
"product of sums" or "AND of ORs"

Each line is a series of terms that are OR'd together. Every line is AND'd together

You can negate a term by prefixing it with `~`

When parsed, all lines starting with `#` and empty lines are ignored

Check the `inputs` directory for examples
