#!/usr/bin/python3.6

import asyncio
controller = Controller()
await controller.connect(
    endpoint='localhost:17070',
    username='admin',
    password='4e308d2a5bbeabaaf8183a34f1494426',
    cacert=None,  # Left out for brevity, but if you have a cert string you
                  # should pass it in. You can get the cert from the output
                  # of The `juju show-controller` command.
)
