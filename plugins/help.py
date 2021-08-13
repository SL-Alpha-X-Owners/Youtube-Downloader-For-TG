from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	alpha2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("🍁 Whatsapp Group 🗯", url="https://chat.whatsapp.com/FOALYW6PMitLo9jntxEGqi")],
		 ])
	help_image = "https://telegra.ph/file/8e3d7e8da2d02d3bd4b75.jpg"
	await message.reply_photo(help_image,  caption="**💌 HELP >**\n• Just Send your Youtube video url🌟 \n• And i will give Method list to select your choice😋\n\n**💌 HELP >**\n• කොපි කරගත් Youtube ලින්කුව එවන්න.\n• එවිට ලැබෙන ලැයිස්තුවෙන් අවශ්‍ය ප්‍රමාණය හා මාදිලිය තෝරාදෙන්න.\n\n\n •😊 This bot is fully free.\n•⚙ Don't pay anyone for Bots like this.",reply_markup=alpha2)
