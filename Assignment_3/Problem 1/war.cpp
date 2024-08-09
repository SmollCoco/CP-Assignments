#include <bits/stdc++.h>
using namespace std;

#define ll  long long int
#define vi  vector<int>
#define vll vector<long long int>

class UnionFind {
    private:
        vi rank, friends;
    public:
        vi enemies; 
        
        UnionFind(int N) {
            friends.assign(N, 0);
            for(int i = 0; i < N; i++)
                friends[i] = i;
            
            rank.assign(N, 0);

            enemies.assign(N, -1); 
        }

        int findSet(int i) {
            if(friends[i] == i)
                return i;
            return friends[i] = findSet(friends[i]);
        }

        bool isSameSet(int i, int j){
            return findSet(i) == findSet(j); 
        }     

        bool areFriends(int x, int y){
            return (findSet(x) == findSet(y)) ? true : false;
        }

        bool areEnemies(int x, int y){
            x = findSet(x);
            y = findSet(y); 
            return (x == enemies[y] or y == enemies[x]) ? true : false;
        }

        void unionSet(int i, int j) {
            if (isSameSet(i,j)) return; 
            
            int x = findSet(i);
            int y = findSet(j);

            if(rank[x] > rank[y])
                swap(x,y);
            
            friends[x] = y; 

            if (rank[x] == rank[y])
                rank[y]++;
        }
};

int main() {
    int n = 0;
    cin >> n;
	
    int c, x, y; 

    UnionFind UF(n);

    while(cin >> c) {

        cin >> x >> y; 
        
        if(c == 1) { 
            if(UF.areEnemies(x,y))
                cout << "-1" << endl;
            else {   
                x = UF.findSet(x);
                y = UF.findSet(y);

                if(UF.enemies[x] == -1 and UF.enemies[y] == -1)
                    UF.unionSet(x,y);   
                
                if(UF.enemies[x] != -1 and UF.enemies[y] == -1)
                {
                    int z = UF.enemies[x];
                    UF.unionSet(x,y);   
                    x = UF.findSet(x);
                    UF.enemies[z] = x;
                    UF.enemies[x] = z;
                }
                
                if(UF.enemies[x] == -1 and UF.enemies[y] != -1)
                {
                    int z = UF.enemies[y];
                    UF.unionSet(x,y);   
                    x = UF.findSet(x);
                    UF.enemies[z] = x;
                    UF.enemies[x] = z;
                }

                if(UF.enemies[x] != -1 and UF.enemies[y] != -1)
                {
                    int a = UF.enemies[x];
                    int b = UF.enemies[y];
                    UF.unionSet(x,y);   
                    UF.unionSet(a,b);   
                    a = UF.findSet(a);
                    x = UF.findSet(x);
                    UF.enemies[x] = a;
                    UF.enemies[a] = x;
                }
            }
        } 

        if(c == 2) {
            if (UF.areFriends(x,y))
                cout << "-1"  << endl;
            else {
                x = UF.findSet(x);
                y = UF.findSet(y);

                if (UF.enemies[x] == y and UF.enemies[y] == x)
                    continue;

                if (UF.enemies[x] == -1 and UF.enemies[y] == -1) {
                    UF.enemies[x] = y;
                    UF.enemies[y] = x;
                }

                if (UF.enemies[x] != -1 and UF.enemies[y] == -1) {
                    int z = UF.enemies[x];
                    UF.unionSet(z,y);
                    int w = UF.findSet(y);
                    UF.enemies[w] = x;
                    UF.enemies[x] = w;
                }

                if (UF.enemies[y] != -1 and UF.enemies[x] == -1) {
                    int z = UF.enemies[y];
                    UF.unionSet(z,x);
                    int w = UF.findSet(x);
                    // New leader may be y or z.
                    UF.enemies[w] = y;
                    UF.enemies[y] = w;
                }

                if (UF.enemies[x] != -1 and UF.enemies[y] != -1) {
                    int a = UF.enemies[x];
                    int b = UF.enemies[y];
                    UF.unionSet(a,y);
                    UF.unionSet(b,x);
                    int p = UF.findSet(x);
                    int q = UF.findSet(y);
                    UF.enemies[p] = q;
                    UF.enemies[q] = p;
                }
            }
        } 

        if(c == 3) {
            if (UF.areFriends(x,y)) cout << "1" << endl;
            else cout << "0" << endl;            
        } 

        if(c == 4) {
            if (UF.areEnemies(x,y)) cout << "1" << endl;
            else cout << "0" << endl;  
        }
    }

	return 0;
}

