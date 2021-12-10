# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL


class Messages:
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\n✅ Send me /help for more info."
      HELP_MSG = [
          ".",
          f"""
**Hey 👋 Welcome back to {PROJECT_NAME}

⚪️ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",
          f"""
**Setting up**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group
""",
          '\x1f**Commands**\x1f\x1f**=>> Song Playing 🎧**\x1f\x1f- /play: Play the requestd song\x1f- /play [yt url] : Play the given yt url\x1f- /play [reply yo audio]: Play replied audio\x1f- /splay: Play song via jio saavn\x1f- /ytplay: Directly play song via Youtube Music\x1f\x1f**=>> Playback ⏯**\x1f\x1f- /player: Open Settings menu of player\x1f- /skip: Skips the current track\x1f- /pause: Pause track\x1f- /resume: Resumes the paused track\x1f- /end: Stops media playback\x1f- /current: Shows the current Playing track\x1f- /playlist: Shows playlist\x1f\x1f*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.\x1f',
          f"""
**=>> Channel Music Play 🛠**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
""",
          f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
          '\x1f**=>> Song Download 🎸**\x1f\x1f- /video [song mame]: Download video song from youtube\x1f- /song [song name]: Download audio song from youtube\x1f- /saavn [song name]: Download song from saavn\x1f- /deezer [song name]: Download song from deezer\x1f\x1f**=>> Search Tools 📄**\x1f\x1f- /search [song name]: Search youtube for songs\x1f- /lyrics [song name]: Get song lyrics\x1f',
          '\x1f**=>> Commands for Sudo Users ⚔️**\x1f\x1f - /userbotleaveall - remove assistant from all chats\x1f - /broadcast <reply to message> - globally brodcast replied message to all chats\x1f - /pmpermit [on/off] - enable/disable pmpermit message\x1f*Sudo Users can execute any command in any groups\x1f\x1f',
      ]
