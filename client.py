# coding:utf-8

import grpc
import data_pb2 as pb2
import data_pb2_grpc as pb2_grpc

_HOST = 'localhost'
_PORT = '8005'


def run():
    conn = grpc.insecure_channel(f'{_HOST}:{_PORT}')
    client = pb2_grpc.TestUnaryStub(channel=conn)
    respone = client.Hello(pb2.HelloRequest(
        name='lee',
        age=999
    ))
    print(respone.result)


if __name__ == "__main__":
    run()
