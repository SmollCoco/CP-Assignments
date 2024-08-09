// Link to YT video: https://youtu.be/B4zCsbjKCAU

#include <bits/stdc++.h>
using namespace std;

int main() {
  int s, d;
  while (scanf("%d %d", &s, &d) != EOF) {
    int i = 4;
    while (s * i - d * (5 - i) > 0)
      --i;

    int choices[5] = {0, 3, 6, 8, 10};
    i = choices[i];

    int res = s * i - d * (12 - i);
    if (res > 0)
      cout << res << '\n';
    else
      cout << "Deficit" << '\n';
  }
}

