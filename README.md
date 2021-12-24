# gRPC PoC

## Prerequisite

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## Generate code
```
$ mkdir protos
$ python -m grpc_tools.protoc -I. --python_out=./protos --grpc_python_out=./protos indentcorp/platform/notid/v1alpha1/message.proto
```


## Load test with K6s


