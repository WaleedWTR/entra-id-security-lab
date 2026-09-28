# Entra ID Security Lab

![Policy tests](https://github.com/WaleedWTR/entra-id-security-lab/actions/workflows/tests.yml/badge.svg)

A portfolio identity-security lab focused on Microsoft Entra ID governance, Conditional Access design, privileged access thinking and sign-in investigation.

> **Portfolio note:** This repository uses synthetic identities, documentation ranges and policy specifications. It contains no tenant, employer or production information.

## What this project demonstrates

- Conditional Access policy design
- MFA and privileged-role protection
- break-glass / emergency-access considerations
- sign-in risk investigation
- identity-focused KQL
- Microsoft Graph PowerShell inventory patterns
- policy-as-code validation
- identity security documentation

## Architecture

```text
Users / Admins / Workloads
           |
           v
       Entra ID
      /   |    \
     /    |     \
   MFA   CA    Roles
     \    |     /
      \   |    /
       Sign-in telemetry
             |
             v
       Investigation
```

## Repository structure

```text
.
├── data/
├── docs/
├── kql/
├── policies/
├── scripts/
└── tests/
```

## Policy approach

The JSON files under `policies/` are **portfolio policy specifications**, not export files intended for direct production import. They make the control intent reviewable without embedding a real tenant configuration.

## Key documentation

- [Identity hardening baseline](docs/identity-hardening.md)
- [Emergency-access design](docs/emergency-access.md)
- [Conditional Access portfolio specification](policies/conditional-access-baseline.json)
- [Sign-in hunting queries](kql/signin-hunting.kql)
- [Technical references](docs/references.md)

## Skills demonstrated

**Microsoft Entra ID · Conditional Access · MFA · Identity Security · Microsoft Graph · KQL · Governance · PowerShell**

## Provenance

This is a sanitised lab/reconstruction. It does not disclose real tenant configuration, users, groups or privileged-role assignments.
