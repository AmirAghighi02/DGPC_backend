<?php

use Illuminate\Foundation\Inspiring;
use Illuminate\Support\Facades\Artisan;
use Illuminate\Support\Facades\Process;

//Artisan::command('inspire', function () {
//    $this->comment(Inspiring::quote());
//})->purpose('Display an inspiring quote')->hourly();

Artisan::command('pint', function () {
    $result = Process::run('./vendor/bin/pint');
    $this->info($result->output());

    return 0;
});
