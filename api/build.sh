npm install
echo 'Build a single swagger file'
multi-file-swagger -o yaml index.yaml > api.yaml
echo 'Validate'
openapi-spec-validator api.yaml --schema 2.0
swagger2openapi api.yaml -o api3.yaml
openapi-spec-validator api3.yaml --schema 3.0.0
