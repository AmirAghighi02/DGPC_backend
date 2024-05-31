<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;

class GetArticles extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'articles:get {file=articles.json} {export=both}';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Command description';

    /**
     * Execute the console command.
     */
    public function handle(): int
    {
        $fileName = $this->argument('file');
        $file = base_path('external/'.$fileName);

        $export = $this->argument('export');

        if (! file_exists($file)) {
            $this->alert('File not found: '.$fileName);
            $this->warn('File must be in external directory');

            return 1;
        }

        if (! in_array($export, ['both', 'db', 'excel'])) {
            $this->alert('Invalid export type: '.$export);
            $this->comment('valid export types: (db, excel, both)');

            return 1;
        }

        $this->handleExport($file, $export);

        return 0;
    }

    protected function addArticlesToDataBase(array $data): void
    {

    }

    protected function saveArticlesToExcel(array $data): void
    {

    }

    protected function handleExport(string $file, string $export)
    {
        $json = file_get_contents($file);
        $data = json_decode($json, true);

        if ($export === 'both') {
            $this->addArticlesToDataBase($data);
            $this->saveArticlesToExcel($data);
        } elseif ($export === 'db') {
            $this->addArticlesToDataBase($data);
        } elseif ($export === 'excel') {
            $this->saveArticlesToExcel($data);
        }
    }
}
