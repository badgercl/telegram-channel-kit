<?php
require_once('telegram_config.php');
function print_updates(){
	$url = "https://api.telegram.org/bot".."/getUpdates";
	$res = file_get_contents($url);
	if($res){
		print_r(json_decode($res, TRUE));
	}
	else{
		echo "Error getting updates";
	}	
}
