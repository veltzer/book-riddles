#include <stdio.h>
#include <stdlib.h>

static int int_to_bits_alt(int value) {
	unsigned int uvalue=*(unsigned*)&value;
	int bits=0;
	while(uvalue!=0) {
		if(uvalue & 1) {
			bits+=1;
		}
		uvalue>>=1;
	}
	return bits;
}

int main(int argc, char** argv, char** envp) {
	int max=1000000;
	int bits=0;
	for(int i=0;i<max;i++) {
		bits+=int_to_bits_alt(i);
	}
	printf("bits is %d\n", bits);
	return EXIT_SUCCESS;
}
