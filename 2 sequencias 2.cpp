#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int rm(int k)
{
    int i = 0, j, ig, vt[100];
    srand(time(0));
    do {
        vt[i] = rand()%100;
        ig = 0;
        for (j = 0; j < i; j++)
        {
            if (vt[j] == vt[i]) ig = 1;
        }
        if (ig == 0) i++;
    } while (i < 100);
    return vt[k];
}
int main()
{
    int i, j, v1[100], v2[100], s1[100], s2[100];
    double f1, f2;
    for (i = 0; i < 100; i++)
    {
        for (j = 0; j < 100; j++)
        {
            v1[j] = 0; v2[j] = 0;
        }
        v1[rm(i)] = 1;
        for(j = 0; j < 100; j++)
        {
            if (v1[j] != v2[j]) break;
        }
        s1[i] = j + 1;
        for(j = 0; j < 100; j++)
        {
            if (v1[rm(rm(j))] != v2[rm(rm(j))]) break;
        }
        s2[i] = j + 1;
    }
    for (i = 0; i < 100; i++)
    {
        f1 = f1 + s1[i];
        f2 = f2 + s2[i];
    }
    f1 = f1/100;
    f2 = f2/100;
    cout << "Sequencialmente a media foi: " << f1 << ".\n";
    cout << "Aleatoriamente a media foi: " << f2 << ".";
}
