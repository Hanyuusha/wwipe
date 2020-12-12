import logging

import attr


@attr.s
class WipeParams(object):
    room_url: str = attr.ib()
    sid: str = attr.ib()

    browser: str = attr.ib(default='firefox')
    headless: bool = attr.ib(default=True)
    knock: bool = attr.ib(default=False)
    fake_media: bool = attr.ib(default=False)
    others_params: dict = attr.ib(default={})
    logger: logging = attr.ib(default=None)
    generator: str = attr.ib(default='zalgo')
    generator_length: int = attr.ib(default=10)
