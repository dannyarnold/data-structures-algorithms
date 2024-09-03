typedef int bool;
enum{false,true};

void comb_sort(int* vector){
    int gap = 20;
    bool permutacion = true;
    int actual;

    while((permutacion)||(gap>1)){
        permutacion=false;
        gap=gap/1.3;
        if(gap<1)gap=1;
        for (actual=0;acutal<20-gap;actual++){
            if(vector[actual]>vector[actual+gap]){
                permutacion=true;

                int temp = vector[actual];
                vector[actual]=vector[actual+gap];
                vector[actual+gap]=temp;
            }
        }
    }
}