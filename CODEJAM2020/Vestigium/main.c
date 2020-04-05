#include<stdio.h>
#include<math.h>
#define ll unsigned long long int
//%llu for scaning and ll for int

int main(){
	int t, n, i, j, k, br, bc, r, c, l, t1;
	scanf("%d", &t);
    t1 = t;
	while(t--)
    {
        scanf("%d", &n);
        int a[n][n];

        for(i=0; i<n; i++)
            for(j=0; j<n; j++)
                scanf("%d", &a[i][j]);
        //Trace
        k = 0;
        for(i=0; i<n; i++)
            k = k + a[i][i];

        //Rows
        r=0;
        for(i=0; i<n; i++)
        {
            br = 0;
            for(j=0; j<n-1; j++)
            {
                for(l=j+1; l<n; l++)
                {
                    if(a[i][j] == a[i][l])
                    {
                        r++;
                        br = 1;
                        break;
                    }
                }
                if(br == 1)
                    break;
            }
        }

        //Columns
        c = 0;
        for(j=0; j<n; j++)
        {
            bc = 0;
            for(i=0; i<n-1; i++)
            {
                for(l=i+1; l<n; l++)
                {
                    if(a[i][j] == a[l][j])
                    {
                        c++;
                        bc = 1;
                        break;
                    }
                }
                if(bc == 1)
                    break;
            }
        }

        printf("Case #%d: %d %d %d\n", (t1-t), k, r, c);
    }
}
