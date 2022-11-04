#include <iostream>
using std::cin;
using std::cout;
#include <string>
using std::string;

int main()
{
 string name, relativeName;
 cout << "Enter your name: \n";
 getline(cin,name);
 cout << "Enter a relative: \n";
 getline(cin,relativeName);

 cout << "Hello.  My name is "<< name <<". You killed my "<< relativeName <<". Prepare to die.";
}

/*
 * CSc103 Project 1: (hello_world++)
 * See readme.html for details.
 */


