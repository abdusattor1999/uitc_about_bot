from data.texts import uitc_alpomish_rasm, kutubxona_rasm, yoshlar_rasm, uitc_alpomish_text,kutubxona_text, yoshlar_text
from aiogram.types import MediaGroup

alpomish_albom = MediaGroup()
for i in uitc_alpomish_rasm:
    alpomish_albom.attach_photo(photo=i)
alpomish_albom.attach_video(video="BAACAgUAAxkBAAPfY3xiNUiD25gRV3wx4nP0epWzW9IAAiEHAAKaa1FVBFHxwVg-lFQrBA", caption=uitc_alpomish_text, parse_mode="HTML")


kutubxona_albom = MediaGroup()
for i in kutubxona_rasm:
    kutubxona_albom.attach_photo(photo=i)
kutubxona_albom.attach_photo(photo="AgACAgIAAxkBAANSY3xdp_HkXSgqd5Xf8BJwziyulyEAAia4MRtYpllIE2c_qTT_L_EBAAMCAAN5AAMrBA", caption=kutubxona_text, parse_mode="HTML")

yoshlar_albom = MediaGroup()
for i in yoshlar_rasm:
    yoshlar_albom.attach_photo(photo=i)
yoshlar_albom.attach_photo(photo="AgACAgIAAxkBAAPmY3xmPhvvR9P25AABSrF7SM-8jqm6AAKwvDEbOg3pS8RK47k_nwwHAQADAgADeQADKwQ", caption=yoshlar_text, parse_mode="HTML")

########################################################################################

async def formatla(son):
    son = str(son)
    a,b = son.split(".")
    javob = f"{a}.{b[:3]}"
    return javob

