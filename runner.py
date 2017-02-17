import asyncio
import zmq
import aiozmq
import uvloop
import time
import os
import aiozmq.rpc

from lua_runner_cython import callCfunc



class ServerHandler(aiozmq.rpc.AttrHandler):

    @aiozmq.rpc.method
    def remote_func(self, a: int, b: int) -> int:
        return callCfunc()


async def go():
    server = await aiozmq.rpc.serve_rpc(
        ServerHandler(), bind='tcp://*:*')
    server_addr = list(server.transport.bindings())[0]

    client = await aiozmq.rpc.connect_rpc(
        connect=server_addr)
    count = 0
    while True:
        ret = await client.call.remote_func(1, 2)
        if ret < 5:
            count += 1
        if count > 5:
            break
        print("Returned from lua -> cythond -> asyncio:", ret)

    server.close()
    await server.wait_closed()
    client.close()
    await client.wait_closed()


def main():
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.get_event_loop().run_until_complete(go())
    print("DONE")


if __name__ == '__main__':
    main()


