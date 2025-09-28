<?php

$date_now = new \DateTime();
$day_number = $date_now->format("N");
$date = $date_now->modify("-1 week");
$date_start = $date->modify("monday this week")->format("Y-m-d 00:00:00");
$date_end = $date->modify("sunday this week")->format("Y-m-d 23:59:59");
$date_end = $date_now->format("Y-m-d H:i:s");
$date_start = $date_now->modify("monday this week")->format("Y-m-d 00:00:00");

date_default_timezone_set('Europe/Moscow');
$current_time = new \DateTime(date("Y-m-d H:i:s"));
$start = $current_time->modify("+1 hour")->format("Y-m-d H:i").":00";
$zoom_end = $zoom_time->modify("+5 minutes")->format("Y-m-d H:i").":59";


// Carbon: в папке laravel/Carbon.md
$month = $carbon->format('n');
$year = $carbon->format('Y');

$item["date_from"] = date('Y-m-d', strtotime($date_from));