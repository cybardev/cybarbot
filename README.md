# Cy | bot

Discord bot interface for my programs

<img height="128px" width="128px" src="./cy-logo.png" alt="ytgo logo">

## Usage

1. Create a bot via Discord Developer Portal.

2. From the left list of tabs, select Installation and copy the Install Link.

3. Visit the Install Link in a browser and add your bot to desired server(s) and/or guild(s).
    - Add scope `application.commands` and `bot` with permissions `Send Messages`, `Send Messages in Threads`, and `Use Slash Commands` to the Invite Link before using it (Discord Developer Portal `>` Installation `>` Guild Install)

4. Deploy bot to Azure Container Apps through [portal.azure.com](https://portal.azure.com)
    - Set the `BOT_TOKEN` environment variable to source from a secret storing your bot's token (Discord Developer Portal `>` Bot `>` Token)
    - Azure was chosen here because it's free and doesn't spin down when idle. Feel free to deploy on a platform of your choice.

5. Test the bot:
    - Send `/say <message>` in a server/guild with the bot to make the bot send a message with the specified content.
    - Send `/yt <query> <embed:optional>` in a server/guild with the bot to return the URL of the first search result on YouTube with the specified query.
    - Send `/resumake <file> <filename:optional>` in a server/guild with the bot and attach a YAML file in [this format](<https://github.com/cybardev/resumake/blob/main/resume.yml> "YAML data input format for Resumake") and give an optional filename to get back a PDF resume.