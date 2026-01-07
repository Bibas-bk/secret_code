#include <stdio.h>
#include "stack.h"
#include "stack.c"

int main() {
    Stack s;
    initStack(&s);

    push(&s, 10);
    push(&s, 20);
    push(&s, 30);

    display(&s);

    printf("Top = %d\n", peek(&s));

    printf("Popped = %d\n", pop(&s));
    display(&s);

    return 0;
}
