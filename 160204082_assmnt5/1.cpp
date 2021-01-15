#include<bits/stdc++.h>
using namespace std;

void A();
void X();
string str;
int f = 0;
int i = 0;
int l ;
int k = 0;
int vi = 0;
int main()
{
    cout<<" A - aXd \n X - bbX \n X - bcX \n X - E "<<endl;
    int n; int c;
    cout<<"How many time do you want to check : ";
    cin>> n;
    for(int j = 0 ; j<n ; j++){
    f = 0;i=0;k=0;
    cout<<"Enter a string : ";
    cin>>str;

    l = str.length();

    if(str[i] == 'a' && str[l-1] =='d'){
        A();
    }
    /*else{
        cout<<"Invalid string "<<endl;
    }*/
    if( l == i && f )
        cout<<"Valid string"<<endl;
    else
        cout<<"Invalid string "<<endl;
    }
    return 0;
}

void A(){
    if(str[i] == 'a'){
        i++;
        f = 1;
        X();
        cout<<i<<endl<<str[i]<<endl;
        if(f == 1 && str[i] == 'd'){
        cout<<"I = "<<i <<"F = "<<f;
        f = 1;
        i++;
        return;
        }
    }
    else{
        f = 0;
        return ;
    }

}

int p = 0;
void X(){
    if(str[i] == 'b'){
            i++;
        if(str[i] == 'b'){
            i++;
            f = 1;
            if(str[i] == 'b'){
                X();
            }
            return;
        }
   else if(str[i] == 'c'){
            i++;
            f = 1;
            if(str[i] == 'b'){
                X();
            }
            return;
        }
    else {
        f = 0;
        return;

        }
    }

}


