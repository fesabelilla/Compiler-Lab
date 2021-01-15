#include<bits/stdc++.h>
using namespace std;

void E();
void T();
void F();
string str;
int f = 0;
int i = 0;
int l ;


int main()
{

    int n;
    cout<<"How many time do you want to check : ";
    cin>> n;
    for(int j = 0 ; j<n ; j++){
    f = 0;i=0;
    cout<<"Enter a string : ";
    cin>>str;

    l = str.length();

    if(l >= 1)
        E();
    else
        cout<<"Invalid string "<<endl;

    if( l == i && f )
        cout<<"Valid string"<<endl;
    else
        cout<<"Invalid string "<<endl;
    //cout<<i<<l<<f;
    }
    return 0 ;
}

void E(){
    T();
    if(str[i] == '+'){
        i++;
        T();
        }
    else if(str[i] == '-'){
        i++;
        T();
        }
}


void T(){
        F();
        if(str[i] == '*'){
            i++;
            f = 1;
            F();
        }
        else if(str[i] == '/'){
            i++;
            f = 1;
            F();
        }
}

void F(){
    if(str[i] == '('){
        //cout<<str[i];
        i++;
        f = 1;
        E();
       }
    if(str[i] == ')'){
        //cout<<str[i];
        i++;
        f = 1;
        return ;
    }
    if((str[i]>='a' && str[i] <= 'e')||(str[i]>='0' && str[i] <= '9')){
       // cout<<str[i];
        i++;
        f = 1;
        return ;
    }
    else{
        f = 0;
        return ;
    }

}
