cat README.md
echo 'Build a single swagger file'
multi-file-swagger -o yaml index.yaml > api.yaml
echo 'Validate'
openapi-spec-validator api.yaml --schema 2.0