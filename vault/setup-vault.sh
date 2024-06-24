#!/bin/bash

# Start Vault in the background
vault server -dev -dev-root-token-id="root" &
sleep 5

# Initialize and unseal Vault
export VAULT_ADDR='http://127.0.0.1:8200'
vault login root

# Enable KV secrets engine
vault secrets enable -version=2 kv

# Add a test secret
vault kv put kv/webapp/config username="admin" password="admin123"
 
