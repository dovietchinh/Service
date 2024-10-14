# SSL (Secure Socket Layer)

## Create a CA

```bash
openssl req \   # make a request
    -new \      # new certificate
    -x509 \     #  X.509 certificate
    -keyout ca-key \  # output file name for key
    -out ca-cert \    # output file name for certificate
    -days 365 \       # duration time for which certificate will be valid
    -subj "/CN=ca.kafka" \   # 
    -nodes \
    -config openssl.cnf

```
