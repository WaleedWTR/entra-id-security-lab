# Emergency Access Design

Emergency-access accounts exist to preserve tenant access if normal administrative controls fail.

## Design considerations

- maintain a very small number of accounts
- use cloud-only identities where appropriate
- use strong, independently protected credentials
- exclude only from controls that could lock out all administrators
- monitor every sign-in attempt
- alert on successful use
- test the procedure periodically
- document who is authorised to access the credentials
- rotate credentials after authorised use

## Important

This repository does not contain real emergency-access account names, secrets or tenant configuration.
