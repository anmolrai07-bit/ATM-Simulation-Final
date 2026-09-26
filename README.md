# Smart ATM Simulation System Using Python

## Overview
A terminal-based ATM simulation demonstrating user registration, card authentication, banking transactions, persistent storage, validation and testing.

## Features
- Multiple users
- Automatic card/account/PIN generation
- Classic, Gold and Platinum cards
- PIN authentication
- Three-attempt card blocking
- Cash withdrawal
- Fast Cash
- Cash deposit
- Balance enquiry
- Fund transfer
- Mini statement
- PIN change
- Card blocking/unblocking
- Daily withdrawal limits
- ATM cash limit
- JSON persistence
- Automated tests

## Requirements
Python 3.9 or later. No external packages are required.

## Run
From the repository root:

```bash
python main.py
```

## Register a User
Select:

```text
2. Register New User
```

Enter the requested details. The program generates a card number, account number and PIN and saves the account in `data/atm_data.json`.

## Use a Card
Select `1. Insert Card`, enter the generated card number and then the PIN.

## Test
Run:

```bash
python -m unittest discover -s tests -v
```

## Project Structure
```text
main.py
atm/
data/
tests/
docs/
README.md
statement.md
requirements.txt
.gitignore
```

## Documentation
See `docs/architecture.md`, `docs/workflow.md`, `docs/diagrams.md` and `docs/design_decisions.md`.

## Academic Note
This is an educational simulation. It does not connect to real banking systems or process real money.
