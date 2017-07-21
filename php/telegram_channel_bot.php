<?php
require_once('telegram_config.php');
function send_post($txt){
	$url = "https://api.telegram.org/bot".TelegramBotConfig::$bot_token."/sendMessage";
	$url .= "?chat_id=".TelegramBotConfig::$channel_id."&parse_mode=".TelegramBotConfig::$parse_mode."&disable_web_page_preview=true&text=$txt";
	$res = file_get_contents($url);
	if($res){
		if(TelegramBotConfig::$show_output){
			print_r(json_decode($res, TRUE));
		}	
	}
	else{
		echo "Error sending the post";
	}
}

