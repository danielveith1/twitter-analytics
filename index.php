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
	<head>
		<title>Twitter App</title>
		
		<link type="text/css" rel="stylesheet" href="index.css"/>
		<link type="text/css" rel="stylesheet" href="http://fonts.googleapis.com/css?family=Source+Sans+Pro|Roboto+Condensed|Oxygen"/>
	</head>
	<body>
		<p class= "table_names">
<?php

echo "RealHughJackman's Tweets and Analytics:\n";
$timeline = $connection->get("statuses/user_timeline", array("screen_name" => "RealHughJackman", "count" => 50, "exclude_replies" => true ));
//$connection->get("statuses/home_timeline", array("screen_name=RealHughJackman"));
//echo count($timeline);
?>
<div id="content">
			<table class="table table-bordered table-condensed table-hover table-striped">
				<tr>
					<th>Tweet Body</th>
					<th>Date Of Tweet</th>
					<th>Number of Retweets</th>
					<th>Number of times Tweet has been Favorited</th>
				</tr>
	
				<?php foreach($timeline as $value){?>
				<tr>
					<td><?php echo $value->text;?></td>
					<td><?php printf($value->created_at); ?></td>
					<td> <?php printf($value->retweet_count); ?> </td>
					<td> <?php printf($value->favorite_count); ?> </td>
                                                        
				</tr>
				<?php } ?>
                                        
			</table>
<?php		

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