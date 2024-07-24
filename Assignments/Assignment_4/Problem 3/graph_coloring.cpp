#include <bits/stdc++.h>
#include <vector>
#include <tuple>

using namespace std;

int m;

void backtrack(vector<int>& color, vector<tuple<int, int>>& edgeList, vector<int>& sum, vector<int>& curr_max, vector<int>& res_x, vector<vector<int>>& res_y, int n);

bool valid(vector<int>& color, vector<tuple<int, int>>& edgeList, vector<int>& sum, vector<int>& curr_max) {
    for (const auto& edge : edgeList) {
        int u = get<0>(edge);
        int v = get<1>(edge);
        if (color[u] && color[v]) {
            return false;
        }
    }
    return sum[0] > curr_max[0];
}

void backtrack(vector<int>& color, vector<tuple<int, int>>& edgeList, vector<int>& sum, vector<int>& curr_max, vector<int>& res_x, vector<vector<int>>& res_y, int n) {
    if (!valid(color, edgeList, sum, curr_max)) {
        for (int v = 1; v <= n; ++v) {
            if (color[v]) {
                color[v] = 0;
                sum[0] -= 1;
                backtrack(color, edgeList, sum, curr_max, res_x, res_y, n);
                color[v] = 1;
                sum[0] += 1;
            }
        }
        return;
    }
    res_x[0] = sum[0];
    res_y[0].clear();
    for (int i = 1; i <= n; ++i) {
        if (color[i]) {
            res_y[0].push_back(i);
        }
    }
    curr_max[0] = sum[0];
    cout << res_x[0] << '\n';
}

int main() {
    cin >> m;
    
    for (int i = 0; i < m; ++i) {
        int n, k;
        cin >> n >> k;
        
        vector<tuple<int, int>> edgeList(k);
        for (int j = 0; j < k; ++j) {
            int u, v;
            cin >> u >> v;
            edgeList[j] = make_tuple(u, v);
        }
        
        vector<int> color(n + 1, 1);
        vector<int> sum(1, n);
        vector<int> curr_max(1, 0);
        vector<int> res_x(1, 0);
        vector<vector<int>> res_y(1);

        backtrack(color, edgeList, sum, curr_max, res_x, res_y, n);
        cout << res_x[0] << endl;
        for (const auto& val : res_y[0]) {
            cout << val << " ";
        }
        cout << endl;
    }
    
    return 0;
}
