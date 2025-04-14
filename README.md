# 🤖 ACM Discord Bot Workshop

Welcome to the ACM Discord Bot Workshop! In this session, we'll guide you through building a feature-rich Discord bot using Python. By the end, you'll have a bot capable of:

- Responding to both traditional (`!`) and modern slash (`/`) commands.
- Assigning roles based on user reactions.
- Sending dynamic embedded messages.
- Generating random numbers upon request.

---

## 🛠️ Features

### ✅ Slash & Prefix Commands

- **`/hello`** Replies with a personalized greeting.
- **`!hello`** Legacy command for greeting user.
- **`/roll`** Generates a random number between 1 and 100.
- **`/embed`** Sends a custom embedded message with specified title, description, and color.

### 🎭 Reaction Role Assignment

- **`/create_role_message`**: Posts a message in a specified channel. Users who react with 👍 to this message will be assigned the 'Member' role.
- The bot listens for reactions to assign or remove roles accordingly.

---

## 🚀 Getting Started

### 1. Clone the Repositry

```bash
git clone https://github.com/your-username/acm-discord-bot.git
cd acm-discord-bot
```

### 2. Install Dependences

Ensure you have Python 3.8 or higher installed. Then, install the required packages.

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variabes

Create a `.env` file in the root directory and add your Discord bot token.

```env
DISCORD_TOKEN=your_bot_token_here
```

### 4. Run the bot

Start the bot using

```bash
python bot.py
```

---

## 📁 Project Strucure

```plaintext
acm-discord-bot/
├── bot.py                  # Main bot script
├── role_message_ids.json   # Stores message IDs for role assignments
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🧪 Testing the Bot

1. **Hello Command**: Type `/hello` or `!hello` in your Discord server to receive a greeting.
2. **Roll Command**: Use `/roll` to get a random number between 1 ad 100.
3. **Embed Command**: Execute `/embed` and provide the required parameters to send a custom embedded mssage.
4. **Role Assignment**
   - Run `/create_role_message`, specifying the channel and role name.
   - The bot will post a message in the chosen channel.
   - Users reacting with 👍 to this message will be assigned the specified role.

---

## 🧰 Additional Notes

- Ensure your bot has the necessary permissions in your Discord server, including managing roles and reading message history.
- The bot uses both traditional command prefixes (`!`) to showcase a deprecated way of doing commands with more modern slash commands (`/`).
- Role assignments are tracked using `role_message_ids.json`. Ensure this file is present and writable.

---

## 📚 Resources

- [discord.py Documentation](https://discordpy.readthedocs.io/)
- [Creating a Discord Bot with Python](https://realpython.com/how-to-make-a-discord-bot-python/)
- [ACM Discord Bot Workshop Materials](https://github.com/your-username/acm-discord-bt)

---

Feel free to customize and expand upon this bot to suit your needs. Happy coding!

---
