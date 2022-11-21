# (c) @RoyalKrrishna

import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", "12124605"))
    API_HASH = os.getenv("API_HASH", "5cf3577d85fd02286535ec2296934287")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5539701008:AAGITX0r-AIYzttZsUcMmXznq1y96h-h-qM")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearchRobot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "1BVtsOJYBu15vseDte4m9vUnDRGJb1fR7hwy36FpZqZ5AU2gDrEggFprZXmX2eKR59iJwCWxsBpjhxnFkZ2jDtDyvTDDU1TEMzEQFMaHeUbjQsSgClfyQOELfIId1Rr9Tk6dAMdP0swWlCVvx5w5BB6MiknZey99zz_7RYR8p9ZQh3yDiaufyD7KQLpKMTcn-yrMXJZR98BWf_yZYYa9DfO8_CUZ8RrGD8Bs37IfPvzeqgYs3BfPZru5HeSswBxfLbqRU8xRm1WXM0jDssXMt3VNut01WoxJxmFq9PpxA5M5MvcsAf2dOrmQjFK08Zdw30ZCVobauNd1EKqP1eJ4bAVmtpAEm4js=")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001697543381"))
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Mdisksearchrobot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "1883570185"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "cyniteofficial")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "cynitebackup")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", "Wait" )
    START_PHOTO = os.getenv("START_PHOTO", https://telegra.ph/file/b57323ed245c34a374ac4.jpg)
    HOME_TEXT = os.getenv("HOME_TEXT", "
Wait" )
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "Cynitemovies")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Okfilterpro:Okfilterpro@cluster0.ec0gpus.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001735125267"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 20))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "cyniteofficial")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "Qu7jX9V0Sn3q1JHdxjPp")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", "Jald")
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", "Soon" )
