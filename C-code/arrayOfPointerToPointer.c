#include <stdio.h>
#include <string.h>

int main() {
    char *student[] = {"Mary", "Bob", "Amber"};
    char *ptStudent[3];
    char **ptPTStudent[3];
    int i, x;

    for (i = 0; i < 3; i++) {
        printf("%s\n", student[i]);
    }
    for (i = 0; i < 3; i++) {
        ptStudent[i] = student[i];
    }
    for (i = 0; i < 3; i++) {
        printf("%s\n", ptStudent[i]);
    }
    for (i = 0, x = 2; i < 3; i++, x--) {
        ptPTStudent[x] = &ptStudent[i];
    }
    for (i = 0; i < 3; i++) {
        printf("%s\n", *ptPTStudent[i]);
    }

    return 0;
}
