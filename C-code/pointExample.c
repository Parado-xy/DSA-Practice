#include <stdio.h>

int main() {
    char letters[2];
    char *ptLetters;
    letters[0] = 'A';
    ptLetters = &letters[0];

    printf("Array Name: %p\n", (void *)letters);
    printf("Pointer Value: %p\n", (void *)ptLetters);

    return 0;
}
