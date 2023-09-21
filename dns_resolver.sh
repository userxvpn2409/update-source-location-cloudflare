#!/bin/bash

DOMAIN="cc220ed01053.sn.mynetname.net"
URL="https://dns.google/resolve?name=$DOMAIN&type=A"

# Sử dụng cURL để gửi yêu cầu HTTP và lấy kết quả trả về
response=$(curl -s "$URL")

# Lấy địa chỉ IP từ kết quả phân giải tên miền
ip=$(echo "$response" | grep -oE '"data":"([^"]+)"' | awk -F'"' '{print $4}')

# In địa chỉ IP
echo "Địa chỉ IP: $ip"
