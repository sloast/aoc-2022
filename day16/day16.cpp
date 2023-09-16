#include <vector>
#include <set>
#include <cassert>
#include <tuple>
#include <unordered_map>
#include <iostream>
#include <map>
#include <utility>
using namespace std;
using ll = long long int;

ll maxt = 26;

ll best = 0;
vector<ll> nodes;
vector<vector<ll>> edges;
using key = tuple<ll, ll, ll, ll>;
map<key, ll> seen = map<key, ll>{};


ll go(ll k, ll t, ll opened, ll prev, ll rem) {
	t--;

	auto ckey = make_tuple(k, t, opened, rem);
	if (seen.count(ckey) == 1) {
		return seen[ckey];
	}

	if (t == 0) {
		if (rem == 0) {
			return 0;
		}
		else {
			ll score = go(0, maxt, opened, -1, rem - 1);
			seen[ckey] = score;
			return score;
		}
	}

	ll score = 0;

	if (((1LL << k) & opened) == 0 && nodes[k] > 0) {
		score =  go(k, t, opened | (1LL << k), -1, rem) + t * nodes[k];
	}
	for (auto& p : edges[k]) {
		if (p != prev) {
			score = max(score, go(p, t, opened, k, rem));
		}
	}

	seen[ckey] = score;

	return score;
}

int main() {
	nodes = vector<ll>{ 0,13,2,20,3,0,0,22,0,21 };
	edges = vector<vector<ll>>{ {3,8,1},{2,0},{3,1},{2,0,4},{5,3},{4,6},{5,7},{6},{0,9},{8} };
	//nodes = vector<ll>{ 0,0,0,0,12,0,18,0,6,8,0,0,22,0,0,0,0,14,0,0,3,0,0,0,0,15,0,0,17,0,0,0,10,0,0,0,25,0,0,0,0,21,13,0,0,0,0,0,11,0,0,9,0,0,0 };
	//edges = vector<vector<ll>>{ {52,39,43,13,34},{29,20},{6,8},{4,9},{3,47,31},{42,54},{23,40,2},{48,52},{2,39,29,15,33},{24,13,46,3,33},{34,20},{51,35},{38},{0,9},{32,17},{31,8},{25,18},{45,40,46,14},{16,42},{51,44},{10,1,24,49,50},{32,23},{36,32},{6,21},{20,9},{16,37},{28,53},{28,37},{26,27},{1,8},{41,48},{15,4},{22,14,44,21},{8,9},{0,10},{36,11},{35,22},{27,25},{12,41},{0,8},{6,17},{38,30},{18,53,5},{51,0},{19,32},{51,17},{17,9},{50,4},{49,7,54,30},{48,20},{20,47},{43,11,45,19},{0,7},{42,26},{48,5} };
	
	ll ans = go(0, 30, 0, -1, 0);
	cout << ans << endl;

	ll ans2 = go(0, maxt, 0, -1, 1);
	cout << ans2 << endl;
}