#include<stdio.h>

int main(int argc,char **argv, char ** envp)
{
	// cppcheck-suppress unusedVariable // teaching: the riddle is printed as posed, its stray variable included
	int i;
	int n = 20;

	// cppcheck-suppress shadowVariable // teaching: the riddle is printed as posed; the loop is what the reader has to repair
	for (int i = 0; i + n; --i) {
		printf("*");
	}
	return 1;
}
