<?php
require_once('dns.php');
$ip = $ipAddress . '/32';
$account_id = '09e1ce4beeee721da60efa2c06287551'; // 
$account_email = 'userxvpn2409@gmail.com'; // 
$api_token = '181af2890ac1bea1646afc0cf12a529fd10d8'; 
$uuid = 'c792b4647b374c618db91abd2d17d323';
$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.cloudflare.com/client/v4/accounts/".$account_id."/gateway/locations/".$uuid,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => "{\n  \"client_default\": true,\n  \"ecs_support\": true,\n  \"name\": \"RouterZTE\",\n  \"networks\": [{\n    \"network\": \"".$ip."\"\n  }]\n}",
  CURLOPT_HTTPHEADER => [
    'Authorization: Bearer ' . $api_token,
    'Content-Type: application/json',
    'X-Auth-Email: ' . $account_email,
    'X-Auth-Key: ' . $api_token
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
