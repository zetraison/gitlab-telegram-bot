# gitlab-telegram-bot
Gitlab telegram bot based on japronto and python-telegram-bot library.

![Python application](https://github.com/zetraison/gitlab-telegram-bot/workflows/Python%20application/badge.svg)

# Usage

### Run container

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
```

### Run pod in kubernetes

```bash
kubectl run gitlab-telegram-bot --image=zetraison/gitlab-telegram-bot:latest \
  --env="TELEGRAM_PROXY_HOST=<proxy_host>" \
  --env="TELEGRAM_PROXY_PORT=<proxy_port>" \
  --env="TELEGRAM_PROXY_USERNAME=<username>" \
  --env="TELEGRAM_PROXY_PASSWORD=<password>" \
  --env="TELEGRAM_BOT_TOKEN=<bot_token>" \
  --env="TELEGRAM_BOT_CHAT_ID=<bot_chat_id>" \
  --env="GITLAB_WEBHOOK_PORT=<gitlab_webhook_port>" \
  --port=8080
  
kubectl expose deployment gitlab-telegram-bot --type=NodePort
```

### Setup GitLab webhook URL

```bash
http://<host>:<gitlab_webhook_port>/webhook
```
