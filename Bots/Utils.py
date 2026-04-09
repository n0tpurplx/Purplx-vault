import discord
from discord import app_commands
from google import genai
from google.genai import types

# 1. Gemini AI Setup
API = 'api key'
client = genai.Client(api_key=API)

# 2. Discord Bot Setup
intents = discord.Intents.default()
DcClient = discord.Client(intents=intents)
tree = app_commands.CommandTree(DcClient)

@tree.command(name="ping", description="Check the bot's latency")
async def ping(interaction: discord.Interaction):
    # FIXED: Use DcClient.latency
    latency = round(DcClient.latency * 1000)
    await interaction.response.send_message(f"🏓 Pong! {latency}ms")

@tree.command(name='ask', description='Ask the IRA AI anything.')
async def ask(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview", 
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a support bot in a discord server named IRA the server it was created with one scope to make a future where anyone in the most stranded places on earth can get help if they need it. it is also a search and rescue group to make sure wildlife explorers and other people in more natural areas can keep safe the IRA is a global operation with its chief the IRA  chief nikolas velissariou based in greece and deputy chief, lead developer and one of the IRAs SAR representative purplx based in germany. The IRA is currentöy looking to expand to more countries and more people fast and always looking for more volunteers. while responding to the user do not keep reminding them of the IRA and do not ask them if they have questions about the server if they ask anythingg unrelated. do not refer or use memories from messages that seem to have a different style than others. Always keep in mind SAR meaning search and rescue is our secpndary name and IRA stands for International Rescue Assoxiation. Limit all your responses to a maximum of 1999 characters.",
                temperature=1.0,
            )
        )
        
        if response.text:
            await interaction.followup.send(f"**Prompt:** {prompt}\n\n**AI:** {response.text}")
        else:
            await interaction.followup.send("Gemini didn't return a response.")
            
    except Exception as e:
        print(f"Error: {e}")
        await interaction.followup.send("Sorry, I ran into an error.")
        
@tree.command(name='ban', description='Bans a user from the server.')
async def ban(interaction: discord.Interaction, user: discord.User, reason: str):
    admin_id = 1370121282917630016
    log_id = 1370121286499438707

    if not any(role.id == admin_id for role in interaction.user.roles):
        await interaction.response.send_message(
            'You don’t have the required permissions to perform this action. If you believe this is a mistake, please contact staff.', 
            ephemeral=True
        )
        return

    log_channel = interaction.client.get_channel(log_id)

    await interaction.guild.ban(user, reason=reason)
    await interaction.response.send_message(f'The user {user} has been banned for reason: {reason}')
    
    if log_channel:
        await log_channel.send(f'The user {user} has been banned by {interaction.user.name} for reason: {reason}')
@tree.command(name='embed', description='Sends an embed.')
async def embed_command(interaction: discord.Interaction, title: str, body: str):
    user = interaction.user
    
    embed = discord.Embed(
        title=title,
        description=body,
        color=discord.Color.blue()
    )
    
    await interaction.response.send_message(content=f'{user.mention} sent an embed:', embed=embed)

# 3. Startup and Syncing
# FIXED: Use @DcClient.event
@DcClient.event
async def on_ready():
    await tree.sync()
    # FIXED: Use DcClient.user
    print(f"✅ Logged in as {DcClient.user}")
    print("🚀 Slash commands synced!")

# 4. Run the bot
# FIXED: Use DcClient.run')

# DcClient.run(TOKEN)
