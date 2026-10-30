#include<stdio.h>

int main(int argc,char **argv, char ** envp)
{
	// cppcheck-suppress unusedVariable
	int i;
	int n = 20;

	// cppcheck-suppress shadowVariable
	for (int i = 0; -i < n; --i) {
		printf("*");
	}
	return 1;
}
