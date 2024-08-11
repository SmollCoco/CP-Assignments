#include <bits/stdc++.h>
using namespace std;

int max(int x, int y) { return (x > y) ? x : y; }

bool isSorted(vector<int> arr) {
  int n = arr.size();

  for (int i = 1; i < n; ++i) {
    if (arr[i - 1] >= arr[i]) return false;
  }

  return true;
}

int main() {
  while (true) {
    int n, m;
    cin >> n;
    cin >> m;
    if (!n && !m) break;

    int matrix[n][m];
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        cin >> matrix[i][j];
      }
    }

    int res = 1;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        for (int p = 0; i + p < n; ++p) {
          for (int q = 0; j + q < m; ++q) {
            vector<int> line;
            for (int a = i; a <= i + p; ++a) {
              for (int b = j; b <= j + q; ++b) {
                line.push_back(matrix[a][b]);
              }
            }

            if (isSorted(line)) res = max(res, line.size());
          }
        }
      }
    }

    cout << res << '\n';
  }

  return 0;
}