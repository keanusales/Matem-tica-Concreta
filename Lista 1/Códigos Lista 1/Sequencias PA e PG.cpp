#include <iostream>
using namespace std;
int main()
{
    int n, i, p = 0;
    double r, q;
    cout << "Qual o tamanho da Sequencia? ";
    cin >> n; //Recebe o tamanho da sequencia
    if (n > 0)
    { //Verifica se o tamanho é positivo
        double v[n]; //Cria o vetor com o tamanho
        for (i = 0; i < n; i++)
        { //Recebe os termos dos vetores
            cout << "Digite o termo " << i+1 << ": ";
            cin >> v[i];
        }
        r = (v[n-1]-v[0])/(n-1); //Calcula a razão da pa
        q = v[1]/v[0]; //Calcula a razão da pg
        for (i = 1; i < n; i++)
        { //Percorre o vetor verificando se é pa
            if (v[i] == v[i-1]+r) p = 1;
            else {p = 0; break;}
        }
        if (p == 0) for (i = 1; i < n; i++)
        { //Se não for pa, percorre verificando se é pg
            if (v[i] == v[i-1]*q) p = 2;
            else {p = 0; break;}
        }
        if (p == 1)
        { //Se for pa, imprime que é pa e o tipo dela
            cout << "A sequencia e uma PA." << endl;
            if (r > 0) cout << "A PA e cescente.";
            else if (r < 0) cout << "A PA e decescente.";
            else cout << "A PA e constante.";
        }
        else if (p == 2)
        { //Se for pg, imprime que é pg e o tipo dela
            cout << "A sequencia e uma PG." << endl;
            if (q == 1) cout << "A PG e constante.";
            else if (q < 0) cout << "A PG e Alternante.";
            else if (q == 0) cout << "A PG e Estacionaria.";
            else if (v[1] > v[0]) cout << "A PG e Crescente.";
            else cout << "A PA e Decrescente.";
        }
        else cout << "A sequencia nao e PA nem PG.";
    }
    else cout << "Digite um numero maior que 0!";
}
