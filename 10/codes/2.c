#include <stdio.h>
#include <math.h>

void linespace(int start, int stop, int step, int* n, int* x, int* y, int num) {
    for (int i = 0; i < num; ++i) {
       n[i]= start + i * step;
        x[i]= pow((2*n[i] -1),2); 
        y[i]= (4*pow(n[i],3)-n[i]+3)/3;
    }
}

int main() {
    // Define the range and step size
    int start = 0;
    int stop = 10;
    int step = 1;

    // Calculate the number of values in the range
    int num = (stop - start) / step + 1;

    // Allocate arrays to store the generated values
    int n[num];
    int x[num];
    int y[num];

    // Call the linespace function
    linespace(start, stop, step, n, x,y, num);

    // Save data to a file
    FILE* file = fopen("output.dat", "w");

    if (file != NULL) {
        for (int i = 0; i < num; ++i) {
            fprintf(file, "%d %d %d\n", n[i], x[i], y[i]);
        }

        fclose(file);
        printf("Data saved to 'output.dat'.\n");
    } else {
        printf("Error opening file for writing.\n");
    }
    
    file = fopen("output.dat", "r");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    //Let us consider some random n, i.e: n1=5
        int n1 = 5;
    double sum = 0;
    for (int i = 0; i < n1+1; ++i) {
        int index;
        double term1;
        double term2;
        fscanf(file, "%d %lf %lf", &index, &term1,&term2);
        sum += term1;
    }
    
       
    
    printf("y(%d) is  %lf\n", n1, sum);
    //to be written in .dat not print
    
    //verifying it using the formula derived in .tex
    //formula
    double  y_n= (4*pow(n1,3)-n1+3)/3;
    printf("y(%d) according to the formula : %lf\n", n1, y_n);
    
    if(y_n == sum)
    {
    	printf("Observed and calculated values are same.\n");
    }
    else
    printf("Error!!!\n");

    return 0;
}
