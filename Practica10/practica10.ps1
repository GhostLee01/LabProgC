$dnsConfig = Get-DnsClientServerAddress -AddressFamily IPv4

Write-Host "Servidores DNS configurados:"
$dnsConfig.ServerAddresses

$domain = "example.com"
$queryResult = Resolve-DnsName -Name $domain

Write-Host "`nRegistros DNS para $($domain):`n"
$queryResult

Write-Host "`nContenido de la caché de DNS:`n"
$dnsCache = Get-DnsClientCache
$dnsCache | Format-Table -AutoSize
