#include <iostream>
using namespace std;
int main()
{
    int t1, t2, i, v = 0;
    cout << "Qual a quantidade de termos da primeira sequencia? ";
    cin >> t1; //Entra com o tamanho da 1ª sequência
    cout << "Qual a quantidade de termos da segunda sequencia? ";
    cin >> t2; //Entra com o tamanho da 2ª sequência
    if (t1 == t2)
    { //Se os tamanhos são iguais, os vetores podem ser iguais
        int v1[t1], v2[t2]; //Faz os vetores com os tamanhos
        for(i = 0; i < t1; i++)
        { //Recebe os termos, um por um, do vetor 1
            cout << "Digite o " << i+1 << "º termo da sequencia 1: ";
            cin >> v1[i];
        }
        for(i = 0; i < t2; i++)
        { //Recebe os termos, um por um, do vetor 2
            cout << "Digite o " << i+1 << "º termo da sequencia 2: ";
            cin >> v2[i];
        }
        for(i = 0; i < t1; i++)
        { //Verifica, índice a índice, se os vetores são iguais
            if (v1[i] != v2[i])
            { v = 1; break; }
            /*Caso sejam diferentes, v é alterdo pra 1, já
            que inicialmente os vetores são iguais, até se
            provar o contrário*/
        }
        if (v == 0) cout << "As sequencias são iguais.\n";
        //Se v é igual a 0, então os vetores são iguais
        else cout << "As sequencias não são iguais.\n";
        //Caso contrário, os vetores são diferentes
        cout << "A quantidade de loops necessários foi " << i << ".";
        /*Com o último índice i pode-se saber a quantidade
        de loops que foram necessários para a verificação*/
    }
    else cout << "As sequencias não são iguais.";
    //Caso contrário, os vetores são diferentes
}
