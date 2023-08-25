from AloneXMusic.core.bot import Alone
from AloneXMusic.core.dir import dirr
from AloneXMusic.core.git import git
from AloneXMusic.core.userbot import Userbot
from AloneXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
