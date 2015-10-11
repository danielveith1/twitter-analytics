<?php
/*ini_set('display_errors',1); 
 error_reporting(E_ALL);
 */
include "twitteroauth-0.6.1/autoload.php";
use Abraham\TwitterOAuth\TwitterOAuth;
include 'password/password.php';
$connection = new TwitterOAuth($ckey, $csecret, $atoken, $asecret);
$content = $connection->get("account/verify_credentials");

?>
<!DOCTYPE html>
<html>
<body>
<p>
<?php

echo "The Tweets of RealHughJackman and the retweets they received.\n";
$timeline = $connection->get("statuses/user_timeline", array("screen_name" => "RealHughJackman", "count" => 50, "exclude_replies" => true ));
//$connection->get("statuses/home_timeline", array("screen_name=RealHughJackman"));
//echo count($timeline);

foreach($timeline as $value){
	
	echo "<p>";
	echo "On ";
	echo $value->created_at;
	echo " the tweet received "; 
	echo $value->retweet_count;
	echo " retweets.";
	
	
	
}

$statuses = $connection->get("statuses/home_timeline", array("count" => 25, "exclude_replies" => true));
/*
echo count($statuses);
foreach($statuses as $value){
	echo $value->;
	echo $value->retweet_count;
	echo $value->created_at;
}
*/
?>

</body>
</html>