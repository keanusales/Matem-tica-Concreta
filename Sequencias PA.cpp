#include <iostream>
using namespace std;
int main()
{
    int n, i, r, p = 0;
    cout << "Qual o tamanho da PA? ";
    cin >> n;
    int v[n];
    for (i = 0; i < n; i++)
    {
        cout << "Digite o termo " << i+1 << " da PA: ";
        cin >> v[i];
    }
    r = (v[n-1]-v[0])/(n-1);
    for (i = 1; i < n; i++)
    {
        if (v[i] != v[i-1]+r) p = 1;
    }
    if (p == 0)
    {
        cout << "A sequencia e uma PA." << endl;
        if (r > 0) cout << "A PA e cescente.";
        else if (r < 0) cout << "A PA e decescente.";
        else cout << "A PA e constante.";
    }
    else cout << "A sequencia nao e uma PA";
}
