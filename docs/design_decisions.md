# Design Decisions

Python was selected because it is the course language and provides JSON, file handling and unittest in the standard library.

A command-line interface was selected so the project runs directly from a terminal without a GUI.

JSON was selected for simple persistent storage without requiring an external database.

The project is split into meaningful modules so account management, authentication, transactions, card generation and storage can be tested and maintained separately.

Different card types demonstrate user-specific withdrawal limits.

The security features are intentionally educational: PIN authentication and failed-attempt blocking are simulated, but the project is not a production banking system.
