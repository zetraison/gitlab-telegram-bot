# gitlab-telegram-bot
Gitlab telegram bot based on japronto and python-telegram-bot library.

# Usage

```bash
docker run -it --rm \
  -e TELEGRAM_PROXY_HOST=<proxy_host> \
  -e TELEGRAM_PROXY_PORT=<proxy_port> \
  -e TELEGRAM_PROXY_USERNAME=<username> \
  -e TELEGRAM_PROXY_PASSWORD=<password> \
  -e TELEGRAM_BOT_TOKEN=<bot_token> \
  -e TELEGRAM_BOT_CHAT_ID=<bot_chat_id> \
  -e GITLAB_WEBHOOK_PORT=<gitlab_webhook_port> \
  zetraison/gitlab-telegram-bot