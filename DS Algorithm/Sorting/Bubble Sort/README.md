## Bubble Sort Algo
  - If array is #of n then #n-1 iteration need.
  - Last 2 elements are sorted automaticatically after each iteration.
  - Best case time complexity is O(n). And, the worst case time complexity is O(n^2).

# Algo

    void bubbleSort(a, n){
         for(i=0; i<n-1; i++){
            flag=0;
            for(j=0; j<n-1-i; j++){
                if(a[j]>a[j+1]){
                    temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                    flag =1;
                }
            }
            if(flag == 0)
               break; //already sorted
         }
    }
