#include<stdio.h>
int linearSearch(int arr[],int key){
   int len=sizeof(arr)/sizeof(arr[0]);
    for(int i=0;i<len;i++){
        if  (arr[i]==key){
            return i;
        }
    }
    return -1;

}
int main(){
    int arr[]={2,3,52,5,66,8,5,7};
    int key;
    printf("Enter the key to search:");
    scanf("%d",&key);
    int  result=linearSearch(arr,key);
    printf("result is %d",result);
    return 0;
}