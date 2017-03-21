#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>


bool gamble()
{
	if (rand() % 5 == 0)
	{
		return true;
	}
	return false;
}

void printflag()
{
	std::cout << "Welcome to our exclusive club!" << std::endl;
	std::ifstream flagI("flag.txt");
	std::string flag;
	getline(flagI, flag);
	flagI.close();
	std::cout << "Here's our special flag: " << flag << std::endl;
}


int networth = 100000;
int main()
{
	std::cout << "Welcome to the EasyCTF 2017 Casino" << std::endl;
	std::cout << "Try your luck and gain access to our exclusive club!" << std::endl;
	while (true)
	{
		std::cout << std::endl;
		std::cout << "Your net worth is: $" << networth << std::endl;
		if (networth > 2000000000)
		{
			printflag();
			break;
		}
		std::cout << "Please enter how much you would like to bet:" << std::endl;
		std::string tmp;
		getline(std::cin, tmp);
		std::stringstream s(tmp);
		int inp;
		s >> inp;
		if (!s.eof() || s.fail())
		{
			std::cout << "That was not a valid number :(";
			continue;
		}
		if (inp <= 0)
		{
			std::cout << "You must bet a positive amount" << std::endl;
			continue;
		}
		if (inp > 100000000)
		{
			std::cout << "Sorry, the most we can allow you to bet is $100,000,000" << std::endl;
			continue;
		}
		if (!gamble())
		{
			std::cout << "Sorry, I'm afraid you've lost :(" << std::endl;
			networth -= inp;
		}
		else
		{
			std::cout << "Congratulations, you won!" << std::endl;
			networth += inp;
		}

	}
	return 0;
}