$pdf_mode = 4;
$lualatex = 'lualatex -halt-on-error -interaction=nonstopmode -file-line-error %O %S';
$out_dir = 'build';
ensure_path( 'TEXINPUTS', './assets//' );