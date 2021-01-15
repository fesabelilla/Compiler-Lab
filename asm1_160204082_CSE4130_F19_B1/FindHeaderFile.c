//Write code for find header file
#include<stdio.h>

int main()
{
    char arr[] = {'#','i','n','c','l','u','d','e'};

    FILE *p1, *p2;
    char c;




    p1 =    fopen("test.c","r");
    p2 = fopen("testHeaderFile.txt","w");
/*
    Natural language processing (NLP) is a
    subfield of linguistics, computer science, information engineering,
    and artificial intelligence concerned with the interactions between
    computers and human (natural) languages,
    in particular how to program computers to
    process and analyze large amounts of natural language data.

*/

    if(!p1)
        printf("Empty\n");
    else{
            int i = 0;
        while((c = fgetc(p1)) != EOF ){
             i++;
// match (#include)
            if(c == arr[i]){

            }
//find header file
            else if(c == '<'){
                while((c = fgetc(p1))){
                    if ( c == '>')
                        break;
                    fputc(c,p2);
                //printf("%c",c);
                }
            }
        }
    }

    fclose(p1);
    fclose(p2);

    p2 = fopen("testHeaderFile.txt","r");

    while((c = fgetc(p2))!= EOF){
        printf("%c",c);
    }
    fclose(p2);

    return 0 ;
}
