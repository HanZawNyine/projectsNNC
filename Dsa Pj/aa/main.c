#include<stdio.h>

int Binary_Search(int arr[],int init, int lastIndex, int searchValue);

int main()
{
int data[5] = {10,20,30,40,50};
int search=20;
int length = sizeof(data) / sizeof(data[0]);
int result =Binary_Search(data,0,length-1, search);
if(result != -1){
    printf("%d Element found at index %d\n",search,result);
}

}

int Binary_Search(int arr[],int init, int length, int searchValue){
    if(length>= init){
        int mid = init + (length - init) / 2;
        //printf("middle index : %d\n",mid);
     //  printf("middle value : %d\n",arr[mid]);
        if(arr[mid]==searchValue){
            return mid;
        }

        if(arr[mid]>searchValue){
            return Binary_Search(arr,init,mid-1,searchValue);
        }
       return Binary_Search(arr,mid+1,length,searchValue);
    }
    return -1;
}
