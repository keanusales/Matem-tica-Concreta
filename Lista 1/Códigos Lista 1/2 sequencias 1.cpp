#include <iostream>
using namespace std;
int main()
{
    int t1, t2, i, v = 0, q = 0;
    cout << "Qual a quantidade de termos da primeira sequencia? ";
    cin >> t1;
    cout << "Qual a quantidade de termos da segunda sequencia? ";
    cin >> t2;
    int v1[t1], v2[t2];
    if (t1 == t2)
    {
        for(i = 0; i < t1; i++)
        {
            cout << "Digite o termo " << i+1 << " da sequencia 1: ";
            cin >> v1[i];
        }
        for(i = 0; i < t2; i++)
        {
            cout << "Digite o termo " << i+1 << " da sequencia 2: ";
            cin >> v2[i];
        }
        for(i = 0; i < t1; i++)
        {
            if (v1[i] != v2[i])
            {
                v = 1;
                break;
            }
        }
        q = q + i + 1;
        if (v == 0) cout << "As sequencias sao iguais.\n";
        else cout << "As sequencias nao sao iguais.\n";
        cout << "A quantidade de casas percorridas foi " << q << ".";
    }
    else
    {
        cout << "As sequencias nao sao iguais.";
    }
}
