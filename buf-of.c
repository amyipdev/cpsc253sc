#include <stdio.h>
#include <stdbool.h>
#include <string.h>
void next_tag(char *s) {
    strncpy(s, "START", 6);
}
int main(int argc, char **argv) {
    bool valid = false;
    char str1[8];
    char str2[8];
    next_tag(str1);
    fgets(str2, 8, stdin);
    // remove newline from fgets
    str2[strcspn(str2, "\n")] = 0;
    if (strncmp(str1, str2, 8) == 0)
        valid = true;
    printf("buffer1: str1(%s), str2(%s), valid(%d)\n", str1, str2, valid);
    return 0;
}