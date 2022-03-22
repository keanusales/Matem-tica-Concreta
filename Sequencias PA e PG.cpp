#include <iostream>
using namespace std;
int main()
{
    int n, i, p = 0;
    double r, q;
    cout << "Qual o tamanho da Sequencia? ";
    cin >> n;
    int v[n];
    for (i = 0; i < n; i++)
    {
        cout << "Digite o termo " << i+1 << " da Sequencia: ";
        cin >> v[i];
    }
    r = (v[n-1]-v[0])/(n-1);
    q = v[1]/v[0];
    for (i = 1; i < n; i++)
    {
        if (v[i] == v[i-1]+r) p = 1;
        else {p = 0; break;}
    }
    if (p == 0) for (i = 1; i < n; i++)
    {
        if (v[i] == v[i-1]*q) p = 2;
        else {p = 0; break;}
    }
    if (p == 1)
    {
        cout << "A sequencia e uma PA." << endl;
        if (r > 0) cout << "A PA e cescente.";
        else if (r < 0) cout << "A PA e decescente.";
        else cout << "A PA e constante.";
    }
    else if (p == 2)
    {
        cout << "A sequencia e uma PG." << endl;
        if (q == 1) cout << "A PG e constante.";
        else if (q == -1) cout << "A PG e Alternante.";
        else if (q == 0) cout << "A PG e Estacionaria.";
        else if (v[n-1] > v[n-2]) cout << "A PG e Crescente.";
        else cout << "A PA e Decrescente.";
    }
    else cout << "A sequencia nao e PA nem PG";
}
