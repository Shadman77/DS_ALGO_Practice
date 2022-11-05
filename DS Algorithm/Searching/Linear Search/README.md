## Linear Search Algo
  - Unsorted Array.
  - Best Time complexity is O(1).
  - Worst Time complexity is O(n).

# Algo

    int linearSearch(a, n, data){

       for(i=0; i<n; i++){
        if(a[i] == data)
            return i; //return the index 
       }
       
       printf("Data not found");
       return -1; //data not found
    }
