#include<stdio.h>
#include "stack.h"
#

void initStack(Stack *s){
    s->top =-1;
}
int  isEmpty(Stack *s){
    return s->top ==-1;
}
int isFull(Stack *s){
    return s->top == MAX-1;
}
void push(Stack *s, int value){
    if(isFull(s)){
        printf("stack overflow");
    }
    s->arr[++(s->top)]=value;
    printf("%d pushed to stack\n",value);

}
int pop(Stack *s){
    if(isEmpty(s)){
        printf("stack underflow/n");
    }
    return s->arr[(s->top)--];
}
int peek(Stack *s){
    if(isEmpty(s)){
        printf("stack is empty\n");
    }
    return s->arr[s->top];
}
void display(Stack *s){
    if(isEmpty(s)){
        printf("stack is empty/n");

    }
    for(int i=s->top;i>=0;i--)
{
    printf("%d\n",s->arr[i]);
}}
