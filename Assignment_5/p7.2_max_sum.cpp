#include <bits/stdc++.h>
using namespace std;

int max(int x, int y) { return (x > y) ? x : y; }

int check(int a, int b, int cumulativeSum[100][100]) {
  if (a < 0 || b < 0)
    return 0;
  else
    return cumulativeSum[a][b];
}

int main() {
  int n;
  cin >> n;

  int matrix[n][n];
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      cin >> matrix[i][j];
    }
  }

  int cumulativeSum[100][100];
  int max_ = -128;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      cumulativeSum[i][j] = check(i - 1, j, cumulativeSum) +
                            check(i, j - 1, cumulativeSum) -
                            check(i - 1, j - 1, cumulativeSum) + matrix[i][j];
      max_ = max(max_, matrix[i][j]);
    }
  }

  int res = -1;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      for (int p = 0; i + p < n; ++p) {
        for (int q = 0; j + q < n; ++q) {
          int subSum = check(i + p, j + q, cumulativeSum) -
                       check(i - 1, j + q, cumulativeSum) -
                       check(i + p, j - 1, cumulativeSum) +
                       check(i - 1, j - 1, cumulativeSum);
          res = max(res, subSum);
        }
      }
    }
  }

  if (max_ < 0) cout << max_;
  else cout << res;
  cout << '\n';

  return 0;
}
