/*
 * CSc103 Project 7: Towers of Hanoi
 * See readme.html for details.
 */

// TODO: write the program.
#include <iostream>
using std::cin;
using std::cout;
using std::endl;
#include <getopt.h> // to parse long arguments.
#include <cstdlib> // for atoi function

/* Here's a skeleton main function for processing the arguments. */
int main(int argc, char *argv[]) {

	void TOH(short n, short start, short end);
	// define long options
	static struct option long_opts[] = {
		{"start",        required_argument, 0, 's'},
		{"end",          required_argument, 0, 'e'},
		{"num-disks",    required_argument, 0, 'n'},
		{0,0,0,0} // this denotes the end of our options.
	};
	// now process the options:
	char c; // to hold the option
	int opt_index = 0;
	short n=0,start=0,end=0; /* to store inputs to the towers function. */
	while ((c = getopt_long(argc, argv, "s:e:n:", long_opts, &opt_index)) != -1) {
		switch (c) {
			case 's': // process option s
				start = atoi(optarg);
				break;
			case 'e': // process option e
				end = atoi(optarg);
				break;
			case 'n': // process option n
				n = atoi(optarg);
				break;
			case '?': // this will catch unknown options.
				// here is where you would yell at the user.
				// although, getopt will already print an error message.
				return 1;
		}
	}


	/* TODO: now that you have the options and arguments,
	 * solve the puzzle. */
	TOH(n,start,end);

	return 0;
}

void TOH(short n, short start, short end) {
	if (n==1) {
		cout<< start <<"\t"<<end<<endl;
		return;
	}
	TOH(n-1, start, 6-start-end);
	cout<< start <<"\t"<<end<<endl;
	TOH(n-1, 6-start-end, end);
}