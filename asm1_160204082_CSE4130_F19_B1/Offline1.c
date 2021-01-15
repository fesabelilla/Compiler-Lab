/*
Id : 16.02.04.082
Section : B1
For ASCII Value
REF : https://theasciicode.com.ar/ascii-
control-characters/horizontal-tab-ascii-code-9.html
*/
#include<stdio.h>
int main()
{
    FILE *p1, *p2;
    char c;

    p1 = fopen("FindHeaderFile.c","r");
    p2 = fopen("offline1.txt","w");

    if(!p1)
        printf("Empty !!\n");
    else
    {
        while((c = fgetc(p1)) != EOF)
        {
             if(c == '/')
            {
                // match (//) and remove single line comment
                if( (c = fgetc(p1)) == '/')
                {
                    while((c = fgetc(p1)) != '\n'){}
                }
                // match (/*) and remove multiple line comment
                else if( c  == '*' )
                {
                    while((c = fgetc(p1)) != '/'){}
                }
            }
             //ascii code of  Space - 32 and horizontalTab = 9
            if( c !=32 && c != 9 && c!='\n' && c!='/')
            {
                 fputc(c,p2);
            }
        }
    }

    fclose(p1);
    fclose(p2);

    p2 = fopen("offline1.txt","r");

    while((c = fgetc(p2))!=EOF)
    {
        printf("%c",c);
    }

    fclose(p2);

    return 0;
}
