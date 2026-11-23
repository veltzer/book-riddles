#include <stdio.h>
#include <stdlib.h>

/*
	This version is ACTUALLY OPTMIZED AWAY BY GCC!!!
	(version 8.3.0 with -O2)
	Amazing!!!
*/
static unsigned int simple() {
	unsigned int i=0;
	unsigned int j;
	do {
		j=i;
		i++;
	} while(i!=0);
	return j;
}

static unsigned int fill_in_ones() {
	unsigned int i=1;
	for(int c=0;c<128;c++) {
		i<<=1;
		i++;
	}
	return i;
}

static unsigned int egg_dropping_riddle() {
	unsigned int i=1;
	unsigned int j=0;
	while(j<i) {
		j=i;
		i<<=1;
	}
	return j | (j-1);
}

/*
	The next version is *without* talking into account
	our knowledge of how numbers are represents in conteporary
	binary architectures
*/
static unsigned int egg_dropping_riddle_better() {
	unsigned int base=0;
	unsigned int jump;
	unsigned int got_to;
	do {
		jump=1;
		got_to=base;
		unsigned int trying_to_get_to=base+jump;
		while(jump*2!=0 && trying_to_get_to>got_to) {
			jump*=2;
			got_to=trying_to_get_to;
			trying_to_get_to=base+jump;
		}
		base=got_to;
	} while(jump>1);
	return got_to;
}


int main(int argc, char** argv, char** envp) {
	printf("the maximal int is %u\n", simple());
	printf("the maximal int is %u\n", fill_in_ones());
	printf("the maximal int is %u\n", egg_dropping_riddle());
	printf("the maximal int is %u\n", egg_dropping_riddle_better());
	return EXIT_SUCCESS;
}
