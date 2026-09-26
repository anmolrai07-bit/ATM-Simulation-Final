# Design Diagrams

## Use Case

```text
User
 |
 +-- Register User
 +-- Insert Card
 +-- Enter PIN
 +-- Withdraw Cash
 +-- Fast Cash
 +-- Deposit Cash
 +-- Check Balance
 +-- Transfer Funds
 +-- View Statement
 +-- Change PIN
 +-- Block/Unblock Card
 +-- Eject Card
```

## Component / Class View

```text
ATMMachine
 |-- Account
 |-- Card
 |-- Authentication
 |-- Transactions
 `-- Storage

Transactions --> JSON Storage
Authentication --> JSON Storage
Account -------> JSON Storage
```

## Sequence: Withdrawal

```text
User -> ATM -> PIN Verification -> Transaction Validation
User <- ATM <- Cash/Receipt <- Account Update <- Storage
```

## Storage Design

```text
atm_data.json
 |
 +-- atm_cash
 `-- users
      `-- card_number
           +-- name
           +-- account
           +-- card_type
           +-- pin
           +-- balance
           +-- daily_limit
           +-- blocked
           `-- transactions[]
```
