# README.md

## Telegram Bot for Skin Scamming

This Telegram bot is created for educational purposes only.

### Overview

This bot allows users to simulate a skin, acc scamming scenario, providing a free skin valued up to $5 every 5 days by rolling a virtual dice. Users can also view available skins through the `/skins` command.

### Prerequisites

To run this bot, you need to obtain an API key from BotFazer and include a fake exchange link for Steam in the code.

### Instructions

1. Clone the repository.
2. Install the required dependencies:

    ```bash
    pip install aiogram
    ```

3. Add your Telegram API token to the `token` variable in the code:

    ```python
    bot = Bot(token='YOUR_TG_API_TOKEN')
    ```

4. Set the path to your skins folder:

    ```python
    skins_folder = 'skins'  # path to your skins folder
    ```

5. Update the fake trade link in the `/rolle` command handler:

    ```python
    await bot.send_photo(message.chat.id, random_skin_image, caption="Congratulations! You won a skin! Confirm the trade using this link\nFAKE_TRADE_LINK")
    ```

### Usage

1. Start the bot using the `/start` command.
2. View available skins with the `/skins` command.
3. Roll the dice and receive a free skin with the `/rolle` command (once every 5 days).

### Disclaimer

This bot is created for educational purposes only. The use of fake trade links and simulated skin, acc scams is strictly discouraged. The developers are not responsible for any misuse or harm caused by this bot.

### Author

[Your Name]

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
