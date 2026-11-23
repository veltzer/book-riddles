#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>

static bool is_one_bit(int v) {
	return (v&(v-1))==0;
}

int main(int argc, char** argv, char** envp) {
	assert(is_one_bit(4)==true);
	assert(is_one_bit(5)==false);
	return EXIT_SUCCESS;
}
