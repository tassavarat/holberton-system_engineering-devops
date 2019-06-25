#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - Sleeps infinitely
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes
 *
 * Return: EXIT_SUCCESS if function properly, otherwise EXIT_FAILURE
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; ++i)
	{
		pid = fork();
		if (pid < 0)
			return (EXIT_FAILURE);
		else if (!pid)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return (EXIT_SUCCESS);
		}
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
