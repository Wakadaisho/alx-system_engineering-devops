#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - infinite sleep
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
 * main - create infinitely-running zombie processes
 * Return: 0
 */

int main(void)
{
	pid_t zombie;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();

		if (zombie)
			printf("Zombie process created, PID: %d\n", zombie);
		else
			return (0);
	}
	infinite_while();
	return (0);
}
