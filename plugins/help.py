from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	alpha2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("🧿 Whatsapp Group 🗯", url="https://chat.whatsapp.com/FOALYW6PMitLo9jntxEGqi")],
		 ])
	help_image = "https://telegra.ph/file/8e3d7e8da2d02d3bd4b75.jpg"
	await message.reply_photo(help_image,  caption="**💡 English HELP 📃...**\n \n__• Just Send your Youtube video url 🌟__ \n__• And i will give Method list to select your choice 😋__\n \n======================\n \n**💡 සින්හල උපදෙස් 📃...**\n \n__• කොපි කරගත් Youtube ලින්කුව එවන්න.__\n__• එවිට ලැබෙන ලැයිස්තුවෙන් අවශ්‍ය ප්‍රමාණය හා මාදිලිය තෝරාදෙන්න.__\n\n•••••••••••••••••••••••\n__• 😊 This bot is fully free.__\n`•⚙ Don't pay anyone for Bots like this.`\n\n⚡ ```Bot By Alpha-X Team``` 🚨\n",reply_markup=alpha2)
