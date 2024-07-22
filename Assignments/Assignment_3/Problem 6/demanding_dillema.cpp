#include <bits/stdcpp.sh>
using namespace std;
 
int matrix[11][33];

int main ()
{
    int testCases;
    scanf ("%d", &testCases);
 
    while (testCases--) {
        int n, m;
        scanf ("%d %d", &n, &m);
 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                scanf("%d", &matrix[i][j]);
        }
 
        bool res = true;
        for (int i = 0; i < m; i++) {
            int sum = 0;
            for (int j = 0; j < n; j++)
                sum += matrix [j] [i];
            if ( sum != 2 ) res = false;
        }
 
        bool v[8 + 3][8 + 3];
        memset(v, false, sizeof(v));
 
        if (res) {
            for (int i = 0; i < m; i++) {
                int first, second, j = 0;
                while (matrix[j++][i] != 1);
                first = j - 1;
                while (matrix[j++][i] != 1);
                second = j - 1;
 
                if (!v[first][second]) v[first][second] = v[second][first] = true;
                else res = false;
            }
        }
 
        if (res) printf ("Yes\n");
        else printf ("No\n");
    }

    return 0;
}

