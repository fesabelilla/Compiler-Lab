#include<bits/stdc++.h>
using namespace std;

void start();
void asgnStart();
void expn();
void extn();
void dcsStart();
void extn1();
void loopStart();
void relop();
void E();
void T();
void F();

string str;
int f = 0;
int i = 0;
int l ;


int main()
{

    cout<<"Enter a string : ";
    cin>>str;

    l = str.length();
    if(l>=1)
     start();
    else
        cout<<"Invalid string "<<endl;

    cout<<l<<" "<<i<<"  "<<f<<str[i]<<endl;
    if( l == i && f == 1 )
        cout<<"Valid string"<<endl;
    else
        cout<<"Invalid string "<<endl;

    return 0 ;
}
void start(){
    asgnStart();
    cout<<"asgsrt"<<f<<endl;
    if(l == i && f == 1) return;

    if(str[i]=='e'){
        f = 1;
        return;
    }

    dcsStart();
    cout<<str[i]<<endl;
    cout<<"dcssrt"<<f<<endl;
    if(l == i && f == 1) return;

    //loopStart();
    //cout<<"loopsrt"<<f<<endl;


    //else{f = 0; return;}
}
void asgnStart(){
    if(str[i] == 'i'){
        i++;
        if(str[i] == 'd'){
            i++;
            if(str[i] == '='){
                i++;
                f = 1;
                expn();
                cout<<"expna"<<f;
                if(f == 1)return;

            }else{ f = 0; return; }

        }else{ f = 0; return; }

    }else{ f = 0; return; }
}

void expn(){
    if(f == 1 ){
        E();
        cout<<"E="<<f<<endl;
        if(f == 1 ){
           extn();
           cout<<"extn"<<f<<endl;

        }else{ f = 0; return; }

    }else{ f = 0; return; }
}
void extn(){
    if(f == 1){
        relop();
        cout<<"relop"<<f<<endl;
        if(f == 1){
            E();
            cout<<"E"<<f<<endl;
        }else{ f = 0; return; }
    }else{ f = 0; return; }
}

//smpl_expn - Start
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
    cout<<"F"<<str[i]<<endl;
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
        cout<<str[i];
        //if(i<l)
            i++;
        f = 1;
        return ;
    }
    else{ f = 0; return; }
}
//smpl_expn - end

void dcsStart(){
    if(str[i] == 'I'){
        i++;
        if(str[i] == 'f'){
            i++;
            if(str[i] == '('){
                f = 1;
                i++;
                expn();
                if(str[i] == ')' && f == 1){
                    i++;
                    f=1;
                    start();
                    cout<<"start : "<<f<<endl;
                    if(f == 1)
                        extn1();
                    else{ f = 0; return; }

                }else{ f = 0; return; }

               }else{ f = 0; return; }

        }else{ f = 0; return; }

    }else{ f = 0; return; }

}

void extn1(){
    if(str[i] == 'e'){
        i++;
        if(str[i] == 'l'){
            i++;
            if(str[i] == 's'){
                i++;
                if(str[i] == 'e'){
                    i++;
                    f = 1;
                    start();
                    if(f == 1){
                        //i++;
                        f = 1;
                        return ;

                    }else{ f = 0; return; }

                }else{ f = 0; return; }

            }else{ f = 0; return; }

        }else{ f = 0; return; }

    }else{ f = 0; return; }
}

void loopStart(){

    if(str[i] == 'w'){
        i++;
       if(str[i] == 'h'){
        i++;
        if(str[i] == 'i'){
            i++;
            if(str[i] == 'l'){
                i++;
                if(str[i] == 'e'){
                    i++;
                    if(str[i] == '('){
                        cout<<"while";
                        i++;
                        f = 1;
                        expn();
                        if(f == 1){
                          if(str[i] == ')'){
                            i++;
                            f = 1;
                            start();

                          } else{ f = 0; return; }

                        } else{ f = 0; return; }

                    } else{ f = 0; return; }

                } else{ f = 0; return; }

            } else{ f = 0; return; }

        } else{ f = 0; return; }

       } else{ f = 0; return; }

    } else{ f = 0; return; }



    if(str[i] == 'f'){
            i++;
            if(str[i] == 'o'){
                i++;
                if(str[i] == 'r'){
                    i++;
                    if(str[i] == '('){
                        i++;
                        f = 1;
                        asgnStart();
                        if(str[i] == ';'&& f == 1){
                            i++;
                            f = 1;
                            expn();
                            if(str[i] == ';' && f == 1){
                                i++;
                                f = 1;
                                asgnStart();
                                if(str[i]==')' && f == 1){
                                    i++;
                                    start();

                                } else{ f = 0; return; }

                        } else{ f = 0; return; }

                        } else{ f = 0; return; }

                    } else{ f = 0; return; }

                } else{ f = 0; return; }

            } else{ f = 0; return; }
    }else{ f = 0; return; }
}

void relop()
{
   /* if(i == l){
        f = 1;
        return;
    }*/
    if(str[i] == '=' || str[i] == '!' ||str[i] == '<'||str[i] == '>'){
        i++;
        if(str[i] == '='){
            i++;
            f = 1;
            return;
        }
    }

    if(str[i] == '>'){
            i++;
            f = 1;
            return;
    }

    if(str[i] == '<'){
            i++;
            f = 1;
            return;
    }
    else{ f = 0; return; }

}


