my @ips;

while (<>) {
    next unless /(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/;
    push(@ips, $1);
}



my %hashh = {};
scalar(%hashh)->{$_}++ for @ips;
my $num=0;
foreach my $name (sort { $hashh{$b} <=> $hashh{$a} } keys %hashh) {
if ($num<10){
    printf "%-8s %s\n", $name, $hashh{$name};
	$num++
	}else{
	last}
	
}
