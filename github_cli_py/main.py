from github_cli_py.src.cli import github_arg_parser

parser = github_arg_parser.GithubArgParser()

if __name__ == "__main__":
  parser.parse()