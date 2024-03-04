#!/bin/bash
set -E

TORR_NAME=$1
TORR_NAME="${TORR_NAME// /_}"                           # замена пробелов подчеркиванием
TORR_NAME=$(echo $TORR_NAME | tr -d {}[])               # удаление скобок
TORR_NAME=$(echo $TORR_NAME - torrent start)            # текст сообщения в чат
JSON_STRING=$( jq -n --arg tn "$TORR_NAME" \            # POST в чат в JSON формате
'{"chat_id": "<YourChatID", "text": $tn}' )
curl -X POST -H 'Content-Type: application/json' \
  -d "${JSON_STRING}" \
  https://api.telegram.org/bot<YourBOTToken>/sendMessage

# Что бы получить chat_id, следует подписаться на обновления в чате: https://api.telegram.org/bot<YourBOTToken>/getUpdates
