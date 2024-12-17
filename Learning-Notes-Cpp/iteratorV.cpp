#include <bits/stdc++.h>
using namespace std;

void reversev(vector<int>::iterator a, vector<int>::iterator b)
{
    if (a != b)
    {
        b--;
        if (a != b)
        {
            while (true)
            {
                swap(*a, *b);
                {
                    a++;
                    if (a == b)
                        break;
                    b--;
                    if (a == b)
                        break;
                }
            }
        }
    }
}
int main()
{
    vector<int> v = {1, 2, 3, 4, 5, 6, 7};
    reversev(v.begin(), v.end());
    for (auto &x : v)
    {
        cout << x << ' ';
    }
}