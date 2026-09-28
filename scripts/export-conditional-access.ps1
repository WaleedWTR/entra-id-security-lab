param(
    [string]$OutputPath = "./conditional-access-export.json"
)

$ErrorActionPreference = 'Stop'

if (-not (Get-Module -ListAvailable Microsoft.Graph.Identity.SignIns)) {
    throw "Microsoft.Graph.Identity.SignIns is required."
}

Import-Module Microsoft.Graph.Identity.SignIns

if (-not (Get-MgContext)) {
    Connect-MgGraph -Scopes "Policy.Read.All"
}

$policies = Get-MgIdentityConditionalAccessPolicy -All

$policies |
    Select-Object Id, DisplayName, State, CreatedDateTime, ModifiedDateTime |
    ConvertTo-Json -Depth 5 |
    Set-Content -Path $OutputPath -Encoding utf8

Write-Host "Exported $($policies.Count) Conditional Access policies to $OutputPath"
