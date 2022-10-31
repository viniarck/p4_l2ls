import asyncio
import os
from kytos.core import KytosNApp, log
from .l2sw_client import L2SWClient
from aiop4 import Client


class Main(KytosNApp):
    """Main class to be used by Kytos controller."""

    async def sw_topo_clients(
        self,
        p4info_path="~/repos/p4_l2ls/l2_switch/l2_switch.p4info.txt",
        config_json_path="~/repos/p4_l2ls/l2_switch/l2_switch.json",
    ) -> list[L2SWClient]:
        """Get L2SWClients for the expected topology, switch attrs will be
        passed as params in the future."""

        p4info_path = os.path.expanduser(p4info_path)
        config_json_path = os.path.expanduser(config_json_path)
        client1 = L2SWClient(Client("localhost:9559", 1), p4info_path, config_json_path)
        client2 = L2SWClient(Client("localhost:9560", 2), p4info_path, config_json_path)
        return [client1, client2]

    async def do_run(self):
        """Start L2Switch clients"""
        log.info("start topo with two switches")
        client1, client2 = await self.sw_topo_clients()
        await asyncio.gather(*[client1.setup_config(), client2.setup_config()])
        await asyncio.gather(*[client1.digests_consumer(), client2.digests_consumer()])

    def setup(self):
        log.info("p4_l2ls napp loaded")
        loop = asyncio.get_running_loop()
        self.task = loop.create_task(self.do_run())
        self.execute_as_loop(3)

    def execute(self):
        if self.task.done():
            try:
                raise self.task.exception()
            except asyncio.InvalidStateError:
                pass

    def shutdown(self):
        self.task.cancel()
