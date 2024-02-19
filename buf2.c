#include <stdio.h>
#include <string.h>
void hello(char *tag) {
    char inp[16];
    printf("Enter value for %s: ", tag);
    fgets(inp, 16, stdin);
    inp[strcspn(inp, "\n")] = 0;
    printf("Hello your %s is %s\n", tag, inp);
}
int main() {
    char *tag = "name";
    hello(tag);
    printf("buffer2 done");
    return 0;
}