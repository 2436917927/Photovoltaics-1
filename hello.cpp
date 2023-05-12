#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct font
{
    char fig[8][20];
    int width;
    char c;
};

struct param
{
    int width;
    char align;
    char msg[100];
};

struct font fonts[37];

struct param parse(int argc, char *argv[]);
void load_fonts();
void display_msg(struct param p);
void display_line(struct param p ,int start, int n);
int calc(struct param p,int start);
struct font getfont(char c);

int main(int argc, char *argv[])
{
    struct param p = parse(argc, argv);
    load_fonts();
    display_msg(p);

}

struct font getfont(char c)
{
    int i;
    for(i=0;i<37;i++)
    {
        if(fonts[i].c == c)
        {
            return fonts[i];
        }
    }
};

int calc(struct param p,int start)
{
    int len = 0;
    int n = 0;
    int i;
    struct font f;
    for(i = start;p.msg[i] != '\0';i++)
    {
        f = getfont(p.msg[i]);
        if(len+f.width<p.width)
        {
            len+=f.width;
            n++;
        }else
        {
            break;
        }
    }
    return n;
}

void display_msg(struct param p)
{
    int n,start=0;
    while((n = calc(p,start)) != 0)
    {
        display_line(p,start,n);
        start+=n;
    }
}

void display_line(struct param p ,int start, int n)
{
    char buf[8][200];
    int i,j;
    int sn;
    struct font f;
    for(i = start;i<start+n;i++)
    {
        f = getfont(p.msg[i]);
        for(j=0;j<8;j++)
        {
            strcat(buf[j],f.fig[j]);
        }
    }
    sn = 0;
    if(p.align=='r')
    {
        sn = p.width - strlen(buf[0]);
    }else if(p.align=='c')
    {
        sn= (p.width - strlen(buf[0]));
    }
    for(i=0;i<8;i++)
    {
        for(j=0;j<sn;j++)
        {
            printf(" ");
        }
        printf("%s\n",buf[i]);
    }
}

void load_fonts()
{
    FILE *fp;
    char cs[]="";
    int i,j,k;
    fp = fopen("nancyj-underlined.flf","r");
    if(fp == NULL)
    {
        exit(0);
    }
    for(i=0;i<10;i++)
    {
        while(fgetc(fp)!= '\n');
    }
    for(i=0;i<strlen(cs);i++)
    {
        for(j=0;j<8;j++)
        {
            fgets(fonts[i].fig[j],20,fp);
            for(k=0;k<strlen(fonts[i].fig[j]);k++)
            {
                if(fonts[i].fig[j][k]=="$")
                {
                    fonts[i].fig[j][k]==" ";
                }
                if(fonts[i].fig[j][k]=="@")
                {
                    fonts[i].fig[j][k]=="\0";
                }
            }
        }
        fonts[i].width=strlen(fonts[i].fig[0]);
        fonts[i].c=cs[i];
    }
    fclose(fp);
}

struct param parse(int argc, char *argv[])
{
    int i;
    struct param p;
    int start = 1;
    p.msg[0]="\0";
    for(i=0;i<argc;i++)
    {
        if(argv[i][0]=='-')
        {
            switch(argv[i][1])
            {
            case 'w':
                p.width=atoi(argv[i+1]);
                if(i+2>start)
                {
                    start =i+2;
                }
                break;
            case 'c':
            case 'r':
            case 'l':
                p.align=argv [i][1];
                if(i+1>start)
                {
                    start = i+1;
                }
                break;
            }
        }
    }
    strcpy(p.msg,argv[start]);
    for(i=start+1;i<argc;i++)
    {
        strcat(p.msg," ");
        strcat(p.msg,argv[i]);
    }
    return p;
};









