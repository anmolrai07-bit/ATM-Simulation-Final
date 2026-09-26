# Workflow

```text
START
  |
  v
Main Menu
  |
  +--> Register New User --> Generate Card/Account/PIN --> Save
  |
  +--> Insert Card --> Find Card --> Verify PIN
                              |
                     +--------+--------+
                     |                 |
                  Correct            Wrong
                     |                 |
                     v              Retry
                  ATM Menu             |
                     |              3 failures
                     v                 |
              Select Transaction       v
                     |              Block Card
                     v
              Validate Request
                     |
                     v
              Update Account
                     |
                     v
                Save Data
                     |
                     v
                   END
```
