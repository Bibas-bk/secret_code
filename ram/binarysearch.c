#include<stdio.h>
int binarysearch(int arr[],int key){
    int low=0;
    int len=sizeof(arr)/sizeof(arr[0]);
    int high=len-1;
    while(low<=high){
        int mid=(low+high)/2;
        if(arr[mid]==key){
            return mid;
                }
        else if(arr[mid]<key){
            low=mid+1;


        }   
        else{
            high=mid-1;
        }     
    }
    return -1;
}
int main(){
    int arr[]={2,3,4,5,6,7,8,9};
    int key;
    printf("Enter the key to search:");
    scanf("%d",&key);
    int result=binarysearch(arr,key);
    printf("%d is found at index %d",key,result);
    return 0;
}
