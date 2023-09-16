#include <vector>
#include <set>
#include <cassert>
#include <tuple>
#include <unordered_map>
#include <iostream>
#include <map>
#include <utility>
#include <algorithm>
#include <iterator>
using namespace std;

vector<vector<int>> blueprints;
vector<int> bp;
int best = 0;

bool part1 = false;
bool part2 = !part1;


int go(int t, int robots[4], int resources[4]) {

	/*cout << "robots: ";
	for (int i = 0; i < 4; i++) {
		cout << robots[i] << ' ';
	}
	cout << endl << "resorcs: ";
	for (int i = 0; i < 4; i++) {
		cout << resources[i] << ' ';
	}
	cout << endl;*/
	
	if (t == 1) {
		int result = resources[3] + robots[3];
		if (result > best) {
			best = result;
			cout << "new best: " << best << ", robots: ";
			for (int i = 0; i < 4; i++) {
				cout << robots[i] << ' ';
			}
			cout << endl;
		}
		//exit(69);
		return result;
	}

	int result = 0;
	bool obflag = false;

	int newRobots[4];
	for (int i = 0; i < 4; i++) {
		newRobots[i] = robots[i];
	}

	if (resources[0] >= bp[4] && resources[2] >= bp[5]) {
		int newResources[4];
		for (int i = 0; i < 4; i++) {
			newResources[i] = resources[i] + robots[i];
		}

		newResources[0] -= bp[4];
		newResources[2] -= bp[5];
		newRobots[3]++;
		return go(t - 1, newRobots, newResources);
		newRobots[3]--;
	}
	if (resources[0] >= bp[2] && resources[1] >= bp[3]) {
		int newResources[4];
		for (int i = 0; i < 4; i++) {
			newResources[i] = resources[i] + robots[i];
		}

		newResources[0] -= bp[2];
		newResources[1] -= bp[3];
		newRobots[2]++;
		result = max(result, go(t - 1, newRobots, newResources));
		newRobots[2]--;
		obflag = true;
		if (t < 10 && !part1) {
			return result;
		}
	}
	if (resources[0] >= bp[1]) {
		int newResources[4];
		for (int i = 0; i < 4; i++) {
			newResources[i] = resources[i] + robots[i];
		}

		newResources[0] -= bp[1];
		newRobots[1]++;
		result = max(result, go(t - 1, newRobots, newResources));
		newRobots[1]--;
		if (part2 && t < 9) {
			return result;
		}
	}
	if (obflag) {
		return result;
	}
	if (resources[0] >= bp[0]) {
		int newResources[4];
		for (int i = 0; i < 4; i++) {
			newResources[i] = resources[i] + robots[i];
		}


		newResources[0] -= bp[0];
		newRobots[0]++;
		result = max(result, go(t - 1, newRobots, newResources));
		newRobots[0]--;
	}
	if (!(resources[2] == 0 && resources[1] < bp[3]-3 && resources[0] >= bp[0] && resources[0] >= bp[1])) {
		int newResources[4];
		for (int i = 0; i < 4; i++) {
			newResources[i] = resources[i] + robots[i];
		}

		result = max(result, go(t - 1, newRobots, newResources));
	}

	return result;
}

int main() {
	//blueprints = vector<vector<int>>{ {4,2,3,14,2,7},{2,3,3,8,3,12},{2,3,3,8,3,12} };
	blueprints = vector<vector<int>>{ {4,4,4,7,2,19},{2,4,4,20,4,18},{4,4,3,20,2,10},{3,4,2,19,2,12},{3,4,3,20,3,14},{3,4,2,15,3,7},{3,3,2,19,2,20},{2,3,3,13,2,20},{2,2,2,8,2,14},{4,4,2,11,3,14},{3,4,4,5,4,8},{3,3,2,16,2,18},{3,4,2,11,2,10},{4,4,2,14,3,17},{3,3,3,19,3,17},{2,4,3,20,2,17},{4,4,3,14,4,8},{2,3,3,9,3,9},{4,4,2,10,3,14},{3,3,2,13,3,12},{4,3,4,15,4,9},{3,3,3,20,2,12},{4,3,4,19,4,12},{4,4,4,15,3,8},{2,3,3,11,2,16},{3,4,3,17,3,7},{4,4,3,7,3,20},{4,3,3,10,2,10},{4,4,4,17,2,13},{4,3,4,20,4,8} };
	int total = 0;

	if (part1) {
		for (int i = 0; i < blueprints.size(); i++) {
			best = 0;
			bp = blueprints[i];
			int startRobots[4] = { 1, 0, 0, 0 };
			int startResources[4] = { 0, 0, 0, 0 };
			int result = go(24, startRobots, startResources);
			cout << "RESULT for BP " << i + 1 << ": " << result << endl << endl;
			total += result * (i + 1);
		}
	}
	if (part2) {
		total = 1;
		for (int i = 0; i < 3; i++) {
			best = 0;
			bp = blueprints[i];
			int startRobots[4] = { 1, 0, 0, 0 };
			int startResources[4] = { 0, 0, 0, 0 };
			int result = go(32, startRobots, startResources);
			cout << "RESULT for BP " << i + 1 << ": " << result << endl << endl;
			total *= result;
		}
	}

	cout << "Total : " << total << endl;
}