# System Architecture

```text
main.py
   |
   v
ATMMachine
   |
   +---- account.py -------- User registration
   +---- card.py ----------- Card/account/PIN generation
   +---- auth.py ----------- PIN and card security
   +---- transactions.py --- Banking operations
   +---- storage.py -------- JSON persistence
   +---- utils.py ---------- Shared helpers
                         |
                         v
                   atm_data.json
```
