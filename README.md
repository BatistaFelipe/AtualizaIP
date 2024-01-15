# AtualizaIP

## Criar arquivo `config.py` com as variáveis abaixo e com as informações coletadas do CloudFlare™
* ZONE_ID: *String*
* DNS_ID: *String*
* API_TOKEN: *String*
* DNS_NAME: *String*

## Modificar a regra de DNS (tipo A) no CloudFlare™
### `getPublicIpAddress()`
```
curl -X PUT "https://api.cloudflare.com/client/v4/zones/<ZONE_ID>/dns_records/<DNS_ID>" \
     -H "Authorization: Bearer <API_TOKEN>" \
     -H "Content-Type: application/json" \
     --data '{
          "content":"<IP_ADDRESS>",
          "name":"<DNS_NAME>",
          "proxied":false,
          "type":"A"
     }'

```

## Ler ip atual do DNS no CloudFlare™
### `getCloudflareIpAdrress()`
```
curl --request GET \
  --url https://api.cloudflare.com/client/v4/zones/zone_identifier/dns_records \
  --header 'Content-Type: application/json' \
  --header 'X-Auth-Email: '
```


## Criar arquivo .exe 
`python3 -m PyInstaller -w -i "icon.ico" --name "AtualizaIP" ".\AtualizaIP.py"`
