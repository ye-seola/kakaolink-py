import asyncio
from kakaolink import IKakaoLinkCookieStorage, IKakaoLinkTokenProvider, KakaoLink


async def main():
    class KakaoLinkCookieStorage(IKakaoLinkCookieStorage):
        def __init__(self):
            self.local_storage = {}

        async def save(self, cookies):
            self.local_storage = cookies

        async def load(self):
            return self.local_storage

    class KakaoTalkTokenProvider(IKakaoLinkTokenProvider):
        async def get_access_token(self) -> str:
            return ""

    kl = KakaoLink(
        default_app_key=,
        default_origin=,
        token_provider=KakaoTalkTokenProvider(),
        cookie_storage=KakaoLinkCookieStorage(),
    )

    await kl.init()
    await kl.send(
        receiver_name=,
        template_id=,
        template_args=,
    )


if __name__ == "__main__":
    asyncio.run(main())
