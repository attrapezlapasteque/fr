

<?php

parse_str($_POST['form-data'], $formdata);//This will convert the string to array

$loosep1  = preg_replace('/\s+/', '_',$formdata['Loosehead-prop_team_1']);
$hooker1  = preg_replace('/\s+/', '_',$formdata['Hooker_team_1']);
$tightp1  = preg_replace('/\s+/', '_',$formdata['Tighthead-prop_team_1']);
$no41     = preg_replace('/\s+/', '_',$formdata['Number-4-lock_team_1']);
$no51     = preg_replace('/\s+/', '_',$formdata['Number-5-lock_team_1']);
$blind1   = preg_replace('/\s+/', '_',$formdata['Blindside-flanker_team_1']);
$no81     = preg_replace('/\s+/', '_',$formdata['Number-8_team_1']);
$open1    = preg_replace('/\s+/', '_',$formdata['Openside-flanker_team_1']);
$scrum1   = preg_replace('/\s+/', '_',$formdata['Scrum-half_team_1']);
$fly1     = preg_replace('/\s+/', '_',$formdata['Fly-Half_team_1']);
$left1    = preg_replace('/\s+/', '_',$formdata['Left-wing_team_1']);
$inside1  = preg_replace('/\s+/', '_',$formdata['Inside-Centre_team_1']);
$outside1 = preg_replace('/\s+/', '_',$formdata['Outside-Centre_team_1']);
$right1   = preg_replace('/\s+/', '_',$formdata['Right-wing_team_1']);
$full1    = preg_replace('/\s+/', '_',$formdata['Fullback_team_1']);

$loosep2  = preg_replace('/\s+/', '_',$formdata['Loosehead-prop_team_2']);
$hooker2  = preg_replace('/\s+/', '_',$formdata['Hooker_team_2']);
$tightp2  = preg_replace('/\s+/', '_',$formdata['Tighthead-prop_team_2']);
$no42     = preg_replace('/\s+/', '_',$formdata['Number-4-lock_team_2']);
$no52     = preg_replace('/\s+/', '_',$formdata['Number-5-lock_team_2']);
$blind2   = preg_replace('/\s+/', '_',$formdata['Blindside-flanker_team_2']);
$no82     = preg_replace('/\s+/', '_',$formdata['Number-8_team_2']);
$open2    = preg_replace('/\s+/', '_',$formdata['Openside-flanker_team_2']);
$scrum2   = preg_replace('/\s+/', '_',$formdata['Scrum-half_team_2']);
$fly2     = preg_replace('/\s+/', '_',$formdata['Fly-Half_team_2']);
$left2    = preg_replace('/\s+/', '_',$formdata['Left-wing_team_2']);
$inside2  = preg_replace('/\s+/', '_',$formdata['Inside-Centre_team_2']);
$outside2 = preg_replace('/\s+/', '_',$formdata['Outside-Centre_team_2']);
$right2   = preg_replace('/\s+/', '_',$formdata['Right-wing_team_2']);
$full2    = preg_replace('/\s+/', '_',$formdata['Fullback_team_2']);




$command = "python main_simulateur.py";
$command .=  " $loosep1 $hooker1 $tightp1 $no41 $no51 $blind1 $no81 $open1 $scrum1 $fly1 $left1 $inside1 $outside1 $right1 $full1 $loosep2 $hooker2 $tightp2 $no42 $no52 $blind2 $no82 $open2 $scrum2 $fly2 $left2 $inside2 $outside2 $right2 $full2   2>&1";


$pid = popen( $command,"r");
 while( !feof( $pid ) )
{
 echo fread($pid, 256);
/*
 flush();
 ob_flush();
 echo "<script>window.scrollTo(0,99999);</script>";
 usleep(100000);
*/
}
pclose($pid);



?>


