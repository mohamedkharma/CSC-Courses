#include <iostream>
#include <chrono>
using namespace std;

void insertionSort( int A[], int n )
{
	for (int i = 1 ; i <= n ; i++)
	{
		int j = i -1;
		int key = A[i];
		while (j > -1 && A[j] >= key ) 
		{
			A[j+1] = A[j];
			j--;
		}
		A[j+1] = key;
	}
}

//============================================
void merge(int array[], int const left, int const mid, int const right)
{
    auto const subArrayOne = mid - left + 1;
    auto const subArrayTwo = right - mid;
 
    // Create temp arrays
    auto *leftArray = new int[subArrayOne],
         *rightArray = new int[subArrayTwo];
 
    // Copy data to temp arrays leftArray[] and rightArray[]
    for (auto i = 0; i < subArrayOne; i++)
        leftArray[i] = array[left + i];
    for (auto j = 0; j < subArrayTwo; j++)
        rightArray[j] = array[mid + 1 + j];
 
    auto indexOfSubArrayOne = 0, // Initial index of first sub-array
        indexOfSubArrayTwo = 0; // Initial index of second sub-array
    int indexOfMergedArray = left; // Initial index of merged array
 
    // Merge the temp arrays back into array[left..right]
    while (indexOfSubArrayOne < subArrayOne && indexOfSubArrayTwo < subArrayTwo) {
        if (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]) {
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
            indexOfSubArrayOne++;
        }
        else {
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
            indexOfSubArrayTwo++;
        }
        indexOfMergedArray++;
    }
    // Copy the remaining elements of
    // left[], if there are any
    while (indexOfSubArrayOne < subArrayOne) {
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
        indexOfSubArrayOne++;
        indexOfMergedArray++;
    }
    // Copy the remaining elements of
    // right[], if there are any
    while (indexOfSubArrayTwo < subArrayTwo) {
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
        indexOfSubArrayTwo++;
        indexOfMergedArray++;
    }
}
 

void mergeSort(int array[], int const begin, int const end)
{
    if (begin >= end)
        return; // Returns recursivly
 
    auto mid = begin + (end - begin) / 2;
    mergeSort(array, begin, mid);
    mergeSort(array, mid + 1, end);
    merge(array, begin, mid, end);
}

//============================================
void max_heapify(int A[], int i , int n )
{
	int largest = i ;
	int left = 2 * i + 1;
	int right = 2 * i +2;
	if ( left <= n && A[largest] <= A[left] )
	{
		largest = left;
	}
	if ( right <= n && A[largest] <= A[right] )
	{
		largest = right;
	}

	if ( largest != i )
	{
		int temp = A[i];
		A[i] = A[largest];
		A[largest] = temp;
		max_heapify ( A, largest , n);
	}

}

void build_heap ( int A[], int n)
{
	for (int i = n/2 ; i >= 0 ; i--)
	{
		max_heapify(A,i,n);
	}
}

void heapSort ( int A[] , int n )
{
	build_heap ( A, n);

	for ( int i = n ; n > 0 ; i--)
	{
		int temp = A[0];
		A[0] = A[n];
		A[n] = temp;
		n = n - 1;
		max_heapify ( A , 0, n );
	}
}

//============================================
// A utility function to swap two elements
void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}
 
int partition (int arr[], int low, int high)
{
    int pivot = arr[high]; // pivot
    int i = (low - 1); // Index of smaller element and indicates the right position of pivot found so far
 
    for (int j = low; j <= high - 1; j++)
    {
        // If current element is smaller than the pivot
        if (arr[j] < pivot)
        {
            i++; // increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}
 
 //QuickSort with  pivot
void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
        at right place */
        int pi = partition(arr, low, high);
 
        // Separately sort elements before
        // partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

//============================================
// Generates Random Pivot and swap
int partition_r(int arr[], int low, int high)
{
    srand(time(NULL));
    int random = low + rand() % (high - low);
    swap(arr[random], arr[high]);
    return partition(arr, low, high);
}
 
//QuickSort with random pivot
void quickSortr(int arr[], int low, int high)
{
    if (low < high) {
 
        /* pi is partitioning index,
        arr[p] is now
        at right place */
        int pi = partition_r(arr, low, high);
 
        // Separately sort elements before
        // partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
//============================================
// A utility function to get maximum value in arr[]
int getMax(int arr[], int n)
{
    int mx = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > mx)
            mx = arr[i];
    return mx;
}
 
// A function to do counting sort of arr[]
void countSort(int arr[], int n, int exp)
{
    int output[n]; 
    int i, count[10] = { 0 };
 
    for (i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;
 
    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];
 
    for (i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
 
    for (i = 0; i < n; i++)
        arr[i] = output[i];
}

// Radix Sort
void radixsort(int arr[], int n)
{
    // Find the maximum number to know number of digits
    int m = getMax(arr, n);
 
    // Do counting sort for every digit. 
    for (int exp = 1; m / exp > 0; exp *= 10)
        countSort(arr, n, exp);
}

//============================================
// A utility function to print an array of size n
void printArray(int arr[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

//============================================
void copy_array(int arrs[], int arrd[], int n) {
    for (int i = 0; i < n; i++)
        arrd[i] = arrs[i];   
}    // arrs for source & arrd for destination

//============================================
int main(){
    int arraysize;
    cout<<"Enter the size of array: ";
    cin>>arraysize;
    int *randArray = new int[arraysize]; //random array with a size of arraysize
    for(int i=0; i<arraysize; i++)
      randArray[i]=rand()%1001;  //Generate number between 0 to 1000
    cout<<"\nArray of size: " << arraysize << " has been created with radom values between 0 and 1000.\nPlease wait while the array get sorted\n" <<endl;

    int *temprandArray = new int[arraysize];
    copy_array(randArray, temprandArray, arraysize);

    cout <<"Random array is: ";
    printArray(randArray, arraysize); //to test the random array

    cout << "\n\n1. ";
	auto start = chrono::steady_clock::now();
    insertionSort(temprandArray, arraysize);
	auto end = chrono::steady_clock::now();
    cout<<"Insertion sort takes: "<< chrono::duration_cast<chrono::nanoseconds>(end-start).count()<<" nanoseconds"<<endl;

    copy_array(randArray, temprandArray, arraysize);
    cout << "2. ";
	auto start1 = chrono::steady_clock::now();
    mergeSort(temprandArray, 0, arraysize-1);
	auto end1 = chrono::steady_clock::now();
    cout<<"Merge sort takes: "<< chrono::duration_cast<chrono::nanoseconds>(end1-start1).count()<<" nanoseconds"<<endl;

    copy_array(randArray, temprandArray, arraysize);
    cout << "3. ";
	auto start2 = chrono::steady_clock::now();
    heapSort(temprandArray, arraysize);
	auto end2 = chrono::steady_clock::now();
    cout<<"Heap sort takes: "<< chrono::duration_cast<chrono::nanoseconds>(end2-start2).count()<<" nanoseconds"<<endl;

    copy_array(randArray, temprandArray, arraysize);
    cout << "4. ";
    auto start3 = chrono::steady_clock::now();
    quickSort(temprandArray, 0, arraysize-1);
	auto end3 = chrono::steady_clock::now();
    cout<<"Quick sort takes: "<< chrono::duration_cast<chrono::nanoseconds>(end3-start3).count()<<" nanoseconds"<<endl;

    copy_array(randArray, temprandArray, arraysize);
    cout << "5. ";
    auto start5 = chrono::steady_clock::now();
    quickSortr(temprandArray, 0, arraysize-1);
	auto end5 = chrono::steady_clock::now();
    cout<<"Quick sort using random pivot takes: "<< chrono::duration_cast<chrono::nanoseconds>(end5-start5).count()<<" nanoseconds"<<endl;

    copy_array(randArray, temprandArray, arraysize);
    cout << "6. ";
    auto start6 = chrono::steady_clock::now();
    radixsort(temprandArray, arraysize);
	auto end6 = chrono::steady_clock::now();
    cout<<"Radix sort takes: "<< chrono::duration_cast<chrono::nanoseconds>(end6-start6).count()<<" nanoseconds.\n\n"<<endl;

    cout << "Sorted Array is: ";
    printArray(temprandArray, arraysize); //to test the random array

    delete [] randArray; // free the heap
    delete [] temprandArray;

    return 0;
}