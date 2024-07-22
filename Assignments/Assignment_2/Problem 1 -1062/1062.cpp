// Youtube link:

#include <bits/stdc++.h>

using namespace std;

int main()
{
    string containers = "";
    int cases = 1;
    cin >> containers;
    while (containers != "end") {
        map<char, int> number_of_containers_left;
        for (const auto& x : containers) {
            if (number_of_containers_left.count(x)) {
                number_of_containers_left[x]++;
            } else {
                number_of_containers_left[x] = 1;
            }
        }
        int number_of_stacks = 1;
        vector<char> top_of_the_stacks;
        top_of_the_stacks.push_back(containers[0]);
        number_of_containers_left[containers[0]]--;
        for (int i = 1; i < containers.length(); i++) {
            for (int j = 0; j < top_of_the_stacks.size(); j++) {
                if (top_of_the_stacks[j] == containers[i]) {
                    number_of_containers_left[containers[i]]--;
                    break;
                }

                else if (top_of_the_stacks[j] >= containers[i]) {
                    top_of_the_stacks[j] = containers[i];
                    number_of_containers_left[containers[i]]--;
                    break;
                }

                else if (j == top_of_the_stacks.size() - 1) {
                    number_of_stacks++;
                    top_of_the_stacks.push_back(containers[i]);
                    number_of_containers_left[containers[i]]--;
                    break;
                }
            }
        }
        cin >> containers;
        cout << "Case " << cases << ": " << number_of_stacks << endl;

        cases++;
    }

    return 0;
}