import discord

import yaml, aiohttp


################################################
# Initialisation 
################################################

try:
    with open('config.yml', 'r') as config_file:
        config_yml = yaml.safe_load(config_file)

        # CF
        cf_token = config_yml['cloudflare']['token']
        cf_acct = config_yml['cloudflare']['account_identifier']
        cf_zone = config_yml['cloudflare']['zone_identifier']

        # Discord
        bot_token = config_yml['discord']['token']
        bot_guilds_whitelist = config_yml['discord']['guilds_whitelist']
        bot_roles_whitelist = config_yml['discord']['roles_whitelist']
except:
    print('Failed to open configuration file! Exiting...')
    quit()

Bot = discord.Bot()
log_prefix = "[CF-via-DISCORD] "

################################################

@Bot.event
async def on_ready():
    print(f"{log_prefix} Discord Bot interface ready.")

@Bot.command(description="View all accessible Lists on Cloudflare.", guild_ids=bot_guilds_whitelist)
async def getlists(ctx):
    await ctx.respond(f"Yoooo this works!!!!!!!!")
    return

Bot.run(bot_token)
