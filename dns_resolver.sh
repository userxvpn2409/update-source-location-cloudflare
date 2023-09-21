#!/bin/bash

DOMAIN="cc220ed01053.sn.mynetname.net"
URL="https://dns.google/resolve?name=$DOMAIN&type=A"

# Sử dụng cURL để gửi yêu cầu HTTP và lấy kết quả trả về
response=$(curl -s "$URL")

# Hiển thị kết quả
echo "Kết quả phân giải tên miền $DOMAIN:"
echo "$response"
