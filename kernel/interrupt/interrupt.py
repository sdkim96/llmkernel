class InterruptHandler:

    def __init__(
        self,
    ) -> None:
        self.devices = {}

    async def register(
        self,
        *,
        device_id: str,
        handler: callable,
    ) -> None:
        self.devices[device_id] = handler


    