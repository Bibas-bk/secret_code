#include<stdio.h>
int linearsearch(int arr[],int n,int key){
	
	int i=0;
	for(i=0;i<n;i++){
		if(arr[i]==key){
			printf("element found at index %d",i);
            return i;
		}
		}
        printf("element not founrd");
        return -1;
	}

int main(){
	int array[]={3,5,6,7,8,3};
    int n=sizeof(array)/sizeof(array[0]);
	linearsearch(array,n,6);
	return 0;
	
}