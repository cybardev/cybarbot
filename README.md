# pycord-template

Discord bot template using Pycord, with instructions on free Render deployment

## Usage

1. Click <kbd>Use this template</kbd> (green button, usually in the top-right area of this page)

2. Select "Create new repository"

3. In your repository, edit the following files:
    - [README.md](./README.md) (this file) for documentation
    - [TERMS.md](./TERMS.md) to reflect your bot's terms of service
    - [PRIVACY.md](./PRIVACY.md) to reflect your bot's privacy policy
    - [bot.py](./bot.py) for main bot functionality
    - [render.yml](./render.yaml) for deployment configuration
    - [requirements.txt](./requirements.txt) and [Dockerfile](./Dockerfile) if your bot requires additional dependencies
    - [.envrc](./.envrc) to change dev shell method or adding environment variables to dev shells
    - [shell.nix](./shell.nix) to modify the dev shell

4. Create a tagged release after you're done editing your bot, and let the GitHub Actions workflow run

5. Create a bot in the [Discord Developer Portal](<https://discord.com/developers/applications> "link to Discord Developer Portal")
    - copy the bot token and store it securely; this will be needed for deployment

6. Deploy bot image to Azure Container Apps through [portal.azure.com](https://portal.azure.com)
    - add your bot token (from step 5) as a Secret and source it to the value of an Environment Variable `BOT_TOKEN` during deployment

7. Add your bot to a Discord server and see it in action

> [!NOTE]
> Azure was chosen here because it's free and doesn't spin down when idle. Feel free to deploy on a platform of your choice.
