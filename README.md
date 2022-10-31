## p4_l2ls

[Kytos-ng](https://github.com/kytos-ng/kytos) P4Runtime L2 learning switch NApp using [aiop4](https://github.com/viniarck/aiop4)

## P4 file

[l2_switch.p4](./l2_switch/l2_switch.p4)

## Dependencies

You'll need to build `simple_switch_grpc` behavioral-model:

- [simple_switch_grpc = "^1.15.0-5ba62db0"](https://github.com/p4lang/behavioral-model/blob/main/targets/simple_switch_grpc/README.md)

### Python

```
python = "^3.9"
p4runtime = "1.4.0rc5"
grpcio = "1.46.3"
googleapis-common-protos = "1.54.0"
protobuf = "3.18.1"
```
## P4 build

```
cd l2_switch
p4c --target bmv2 --arch v1model --p4runtime-files l2_switch.p4info.txt l2_switch.p4
```
