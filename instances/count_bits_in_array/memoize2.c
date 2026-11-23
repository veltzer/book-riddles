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
	char table[256*256];
	for(int i=0;i<256*256;i++) {
		table[i]=int_to_bits_alt(i);
		//printf("table at point %d is %d\n", i, table[i]);
	}
	int max=1000000;
	int bits=0;
	for(int i=0;i<max;i++) {
		unsigned int u=(unsigned int)i;
		bits+=table[u & 0xffff];
		bits+=table[(u >> 16) & 0xffff];
	}
	printf("bits is %d\n", bits);
	return EXIT_SUCCESS;
}
