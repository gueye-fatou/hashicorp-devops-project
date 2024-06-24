#!/bin/bash

# Start Consul in the background
consul agent -dev -bind 127.0.0.1 &

# Create a Consul service definition file for the Flask app
cat <<EOF > /etc/consul.d/web.json
{
  "service": {
    "name": "web",
    "tags": ["web"],
    "port": 80
  }
}
EOF

# Register the web service
consul services register /etc/consul.d/web.json
 
