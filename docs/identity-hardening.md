# Identity Hardening Baseline

## Control objectives

### Privileged identities

- require strong MFA
- minimise standing privilege
- separate administrative and everyday-use accounts where appropriate
- monitor privileged sign-ins
- protect emergency-access accounts with independent controls and monitoring

### Conditional Access

Introduce policies in a controlled sequence:

1. define target population
2. identify emergency-access exclusions
3. model expected impact
4. use report-only mode
5. review sign-in results
6. remediate incompatible applications
7. enable enforcement
8. monitor and periodically review

### Legacy authentication

Legacy authentication protocols should be identified and retired where they cannot support modern authentication controls.

### Identity monitoring

Useful signals include:

- repeated sign-in failures
- unusual geographies
- unfamiliar devices
- Conditional Access failures
- risky sign-ins
- privileged-role activity

## Governance principle

Identity controls should be treated as a service: documented ownership, change control, exception management, telemetry, testing and periodic review.
