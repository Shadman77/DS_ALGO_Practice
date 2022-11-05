## Binary Search Algo
  - It's Faster Than Linear Search.
  - It's Follow The divide and conqure rule.
  - The Time Worst Time Complixity is O(logn), And Best Time Complixity is O(1).
  - The Array Must be sorted.
  - If l>r that means data not found in array.

# Algo

    binarySearch(a, n, data){

        l = 0, r = n-1;

        while(l<r){
                mid = (l+r)/2;

                if(data == a[mid])
                     return mid;
                else if(data < a[mid])
                     r = mid-1;
                else 
                     l = mid+1;
        }
        return -1;
    }
