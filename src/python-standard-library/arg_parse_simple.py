import argparse


def print_arg(args: argparse.Namespace):
    print(f'    |> NAMESPACE CREATED: {args.__dict__}\n')


level_1_parser = argparse.ArgumentParser(
    description='This application is intended to teach you how to use argparse lib'
)

# Add arguments in first level. Example: >>> python file.py --arg1 hello
level_1_parser.add_argument('--arg1', default='default_value 1', help='arg 1 example of help')
level_1_parser.add_argument('--arg2', default='default_value 2')

# Add function to the parser to be called later. In other words, a funtion pointer
level_1_parser.set_defaults(func_1=print_arg)

# Add fixed attribute to the parser.
level_1_parser.set_defaults(fixed_attribute='fixed_value')


# Add second level parse. Example >>> python file.py sub --argsub 42
level_2_parser = level_1_parser.add_subparsers()
parser_foo = level_2_parser.add_parser('sub')
parser_foo.add_argument('--argsub', type=int)

# Build arguments structure
arguments_strucure = level_1_parser.parse_args()

# Calling the function created dinamically
arguments_strucure.func_1(arguments_strucure)
