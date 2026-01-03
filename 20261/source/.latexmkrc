# Detect OS and set path separator
my $sep = ($^O =~ /Win/) ? ';' : ':';
my $root = $ENV{'WORKSPACE_FOLDER'} // '..';

$ENV{'TEXINPUTS'} = ".$sep$root/20261/source//$sep";

use File::Path qw(make_path);
make_path('tikz-cache');

$pdf_mode = 1;
$pdflatex = 'pdflatex -shell-escape -interaction=nonstopmode -file-line-error %O %S';