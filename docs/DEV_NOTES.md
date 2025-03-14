# Planning/Layout Scratchpad

## Features Checklist Macro-View

- [ ] Access Github Events API
  - [ ] Save token to access private events log?
- [ ] CLI
  - [ ] options to filter activity?
- [ ] Settings
  - [ ] settings file loaded on init?
- [ ] Visualize activity
  - [ ] Ascii visualization libraries?
- [ ] Graceful error handling
- [ ] Poetry dev scripts?

## Things To Look Up

- Static typing conventions
  - https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#cheat-sheet-py3
- Packaging
  - https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/

## Libraries Used

- [requests](https://requests.readthedocs.io/en/latest/):
  - Interacting with Github Events REST API
- ABC
  - Practice using abstract base classes to bake better OOP practices into projects
- argparse
  - CLI parser
- pytest
  - To assist in test-driven development
- rich
  - plotting in terminal
- pydantic
  - Github response model validation
- mypy
  - static type checking
- typing
  - type hints
