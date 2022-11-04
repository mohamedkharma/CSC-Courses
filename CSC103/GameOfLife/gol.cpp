/*
 * CSc103 Project 3: Game of Life
 * See readme.html for details.
 */

#include <cstdio>
#include <stdlib.h> // for exit();
#include <getopt.h> // to parse long arguments.
#include <unistd.h> // sleep
#include <vector>
using std::vector;
#include <string>
using std::string;
#include <iostream>

using namespace std;

static const char* usage =
"Usage: %s [OPTIONS]...\n"
"Text-based version of Conway's game of life.\n\n"
"   --seed,-s     FILE     read start state from FILE.\n"
"   --world,-w    FILE     store current world in FILE.\n"
"   --fast-fw,-f  NUM      evolve system for NUM generations and quit.\n"
"   --help,-h              show this message and exit.\n";

size_t max_gen = 0; /* if > 0, fast forward to this generation. */
string wfilename =  "/tmp/gol-world-current"; /* write state here */
FILE* fworld = 0; /* handle to file wfilename. */
string initfilename = "/tmp/gol-world-current"; /* read initial state from here. */

/* NOTE: you don't have to write these functions -- this is just how
 * I chose to organize my code. */
size_t nbrCount(size_t i, size_t j, const vector<vector<bool> >& g);
void update();
int initFromFile(const string& fname); /* read initial state into vectors. */
void mainLoop(vector<vector<bool> >world);
void dumpState(FILE* f);

/* NOTE: you can use a *boolean* as an index into the following array
 * to translate from bool to the right characters: */
char text[3] = ".O";

int main(int argc, char *argv[]) {
	// define long options
	static struct option long_opts[] = {
		{"seed",    required_argument, 0, 's'},
		{"world",   required_argument, 0, 'w'},
		{"fast-fw", required_argument, 0, 'f'},
		{"help",    no_argument,       0, 'h'},
		{0,0,0,0}
	};
	// process options:
	char c;
	int opt_index = 0;
	while ((c = getopt_long(argc, argv, "hs:w:f:", long_opts, &opt_index)) != -1) {
		switch (c) {
			case 'h':
				printf(usage,argv[0]);
				return 0;
			case 's':
				initfilename = optarg;
				break;
			case 'w':
				wfilename = optarg;
				break;
			case 'f':
				max_gen = atoi(optarg);
				break;
			case '?':
				printf(usage,argv[0]);
				return 1;
		}
	}
	/* NOTE: at this point wfilename initfilename and max_gen
	 * are all set according to the command line: */
	//printf("input file:  %s\n",initfilename.c_str());
	//printf("output file: %s\n",wfilename.c_str());
	//printf("fast forward to generation: %lu\n",max_gen);
	/* TODO: comment out 3 lines above once you see what's in them. */
	/* NOTE: if wfilename == "-" you should write to stdout, not a file
	 * named "-"! */

	/* If you wrote the initFromFile function, call it here: */
	initFromFile(initfilename);

	int ppid = getppid();
	char mypid[6];
	sprintf(mypid, "%d", ppid);
	wfilename = "/proc/";
	wfilename.append(mypid);
	wfilename.append("/fd/1");


	vector<vector<bool> > world;
	FILE* f = fopen(initfilename.c_str(),"rb"); /* note conversion to char* */
	world.push_back(vector<bool>()); /* add a new row */
	size_t rows = 0;/* current row we are filling */
	char d;
	while (fread(&d,1,1,f)) {
    if (d == '\n') {
        /* found newline; add a new row */
        rows++;
        world.push_back(vector<bool>());
    } else if (d == '.') {
        world[rows].push_back(false); /* dead x_x */
    } else {
        world[rows].push_back(true); /* alive 8D */
    }
}
	world.pop_back();
	fclose(f);

	mainLoop(world);
	return 0;
}


void mainLoop(vector<vector<bool> > world) {
	/* TODO: write this */
	/* update, write, sleep */
	size_t row=world.size();
	size_t column=world[0].size();
	if (max_gen == 0) {
		while(true) {
			vector<vector<bool> > future(world);
				for(size_t i=0; i<world.size(); i++){ //prints rows
					for(size_t j=0; j<world[i].size(); j++){ // prints columns
						size_t alive = 0;

//The following code will test all of the eight neighbors positions for any alive neighbors.
						if(world[i][(j+1+column)%column] == 1) {
							alive++;
						}
						if(world[i][(j-1+column)%column] == 1) {
							alive++;
						}
						if(world[(i-1+row)%row][j] == 1) {
							alive++;
						}
						if(world[(i+1+row)%row][j] == 1) {
							alive++;
						}
						if(world[(i-1+row)%row][(j+1+column)%column] == 1) {
							alive++;
						}
						if(world[(i-1+row)%row][(j-1+column)%column] == 1) {
							alive++;
						}
						if(world[(i+1+row)%row][(j+1+column)%column] == 1) {
							alive++;
						}
						if(world[(i+1+row)%row][(j-1+column)%column] == 1) {
							alive++;
						}
//At this point, the program should have checked how many alive neighbors there are and recoreded them in alive++.

						if(world[i][j] == 1 && (alive > 3 || alive < 2)) { //if there are more than 3 neighbors, or less than 2 neighbors, it dies.
							future[i][j] = 0;
						}
						else if (world[i][j] == 0 && alive == 3) { //if there are exactly 3 neighbors, it comes to life.
							future[i][j] = 1;
						}
					}
				}

			world = future;

			FILE* f = fopen(wfilename.c_str(),"wb");
			char c = '.';
			char d = 'O';
			char e = '\n';
			for(size_t i=0; i<row; i++){
				for(size_t j=0; j<column; j++){
					if(world[i][j]==0){
						fwrite(&c,1,1,f);
					}
					else{
						fwrite(&d,1,1,f);
					}
				}
				fwrite(&e,1,1,f);
			}
			fclose(f);

			sleep(1);
		}

		/* make one generation update per second */
	}


	else {
		/* go through generations as fast as you can until
		 * max_gen is reached... */
		size_t min = 0;
		while(min<max_gen) {
			min++;
			vector<vector<bool> > future(world);
				for(size_t i=0; i<world.size(); i++){ //prints rows
					for(size_t j=0; j<world[i].size(); j++){ // prints columns
						size_t alive = 0;

	//The following code will test all of the eight neighbors positions for any alive neighbors.
							if(world[i][(j+1+column)%column] == 1) {
								alive++;
							}
							if(world[i][(j-1+column)%column] == 1) {
								alive++;
							}
							if(world[(i-1+row)%row][j] == 1) {
								alive++;
							}
							if(world[(i+1+row)%row][j] == 1) {
								alive++;
							}
							if(world[(i-1+row)%row][(j+1+column)%column] == 1) {
								alive++;
							}
							if(world[(i-1+row)%row][(j-1+column)%column] == 1) {
								alive++;
							}
							if(world[(i+1+row)%row][(j+1+column)%column] == 1) {
								alive++;
							}
							if(world[(i+1+row)%row][(j-1+column)%column] == 1) {
								alive++;
							}
	//At this point, the program should have checked how many alive neighbors there are and recoreded them in alive++.

							if(world[i][j] == 1 && (alive > 3 || alive < 2)) { //if there are more than 3 neighbors, or less than 2 neighbors, it dies.
								future[i][j] = 0;
							}
							else if (world[i][j] == 0 && alive == 3) { //if there are exactly 3 neighbors, it comes to life.
								future[i][j] = 1;
							}
						}
					}
					world = future;

			FILE* f = fopen(wfilename.c_str(),"wb");
			char c = '.';
			char d = 'O';
			char e = '\n';
			for(size_t i=0; i<world.size(); i++){
				for(size_t j=0; j<world[0].size(); j++){
					if(world[i][j]==0){
						fwrite(&c,1,1,f);
					}
					else{
						fwrite(&d,1,1,f);
					}
				}
				fwrite(&e,1,1,f);
			}
			fclose(f);
		}

	}
}


int initFromFile(const string& fname) {
	/* Open the file (for reading), storing the handle in f: */
	FILE* f = fopen(fname.c_str(), "rb");
/* make sure file was opened properly: */
	if (!f) {
    // deal with error by printing a message, or maybe quitting
    // the entire program with a non-zero exit code, like this:
    exit(1);
		return 1;;
	}
	fclose(f);
	return 0;
}
