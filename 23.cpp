#include <bits/stdc++.h>
using namespace std;

// M * N is tiny
int M, N;
vector<string> G;
vector<vector<bool>> visited;

vector<int> pos;

void dfs(int r, int c, int cur, bool p1) {
  if (r < 0 || r >= M) return;
  if (c < 0 || c >= N) return;
  if (G[r][c] == '#') return;
  if (visited[r][c]) return;

  if (r == M - 1) {
    pos.push_back(cur);
  }

  visited[r][c] = true;

  if (G[r][c] == '^' && p1) {
    dfs(r-1, c, cur+1, p1);
  } else if (G[r][c] == 'v' && p1) {
    dfs(r+1, c, cur+1, p1);
  } else if (G[r][c] == '>' && p1) {
    dfs(r, c+1, cur+1, p1);
  } else if (G[r][c] == '<' && p1) {
    dfs(r, c-1, cur+1, p1);
  } else {
    dfs(r+1, c, cur+1, p1);
    dfs(r-1, c, cur+1, p1);
    dfs(r, c+1, cur+1, p1);
    dfs(r, c-1, cur+1, p1);
  }

  visited[r][c] = false;
}

int main() {
  fstream fin("input.txt");

  string line;
  while (fin >> line) {
    G.push_back(line);
  }
  M = G.size();
  N = G[0].size();
  visited = vector(M, vector<bool>(N));

  dfs(0, 1, 0, true);
  cout << *max_element(pos.begin(), pos.end()) << std::endl;
  pos.clear();

  dfs(0, 1, 0, false);
  cout << *max_element(pos.begin(), pos.end()) << std::endl;
}
