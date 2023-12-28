echo "please enter the singer name: \c"
read singer
case $singer in
	[bB]alu)
		first_album=Balu_first
		last_album=Balu_last
		;;
	"Devi Sri")
		
		first_album=Devisri_first
		last_album=Devisri_last
		;;
	Jesudas)
		first_album=Jesudas_first
		last_album=Jesudas_last
		;;
	*)
		echo "unknow author"
		exit
		;;
esac
echo "the singer is $singer; His first album is: $first_album and last album is $last_album"
