import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28617319"))
    API_HASH = os.environ.get("API_HASH", "15e0d554ea25e629d21b9d9d7457d3ff")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5490753736:AAFASmAONuTMKggKB9WkOfdst2MV7YBkeDE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzQBuzlIdOUGnfSAS84r3T5MDe-2J9M7FUbCANqMm8s7a7YXZQ-qA6EzbfN0-h0EOCeTD9MZ-L1YpaabXqFf5uGMnMq8KDl5bMwK_-MIdQAzE8ecl56CgO6qJl0w0jd2rqj45iP_smQKXJGoLp7tZQ1fAm5OphBII4mApox1C7Ku468ByYo8PsFVqpRrtgLDpJFbvorVoJIr4yxeb_F2zcq_Qsl5WM4R9INJHBI0oAlAMUESgSr8InyWkxMwSyVfqQF5jpLDDFGhf7Vf_NmTaRe-XA4_7bpZSbpxnOKvnzPaPXG07NzQi8LuvivAU5dEDocWxwP5aV3kSp7gP3ilFX2fj6M=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "x_eternal_musicbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5826154814")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
