"""bot.py -- main file"""

import logging
import os

import discord
import dotenv

# PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv.load_dotenv()

# dotenv.load_dotenv(os.path.join(PARENT_DIR, ".env"))


def create_bot() -> discord.Client:
    """`create_bot`

    Create a new instance of a Discord bot.

    returns:
        - `discord.Client`: The bot instance
    """

    intents = discord.Intents()
    intents.voice_states = True
    _client = discord.Client(intents=intents)

    @_client.event
    async def on_voice_state_update(
        member: discord.Member, before: discord.VoiceState, after: discord.VoiceState
    ) -> None:
        """kicks saaketh

        args:
            - `member (discord.Member)`: The member that was updated
            - `before (discord.VoiceState)`: The member's voice state before the update
            - `after (discord.VoiceState)`: The member's voice state after the update
        """
        if member.id == 662832706677375009:
            await member.move_to(None)
            logging.info("kicked Saaketh")
        return

    return _client


if __name__ == "__main__":
    client = create_bot()
    client.run(os.getenv("DISCORD_TOKEN"))
