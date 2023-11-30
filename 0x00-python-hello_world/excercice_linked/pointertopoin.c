#include <stdio.h>

void modifyPointer(int** ptr) {
    int data = 20;
    *ptr = &data;

    printf("Value of pointer ptr inside the functio is: %p\n", ptr);               // Output: 10

}

int main() {
    int data = 10;
    int* ptr = &data;
    int** ptrToPtr = &ptr;

    printf("Value of data: %d\n", data);                      // Output: 10
    printf("Value of pointer *ptr: %d\n", *ptr);               // Output: 10
    printf("Value of pointer **ptrToPtr: %d\n", **ptrToPtr);   // Output: 10

    printf("Value of pointer ptr: %p\n", ptr);               // Output: 10
    printf("Value of pointer *ptrToPtr: %p\n", *ptrToPtr);   // Output: 10
    printf("Value of pointer ptrToPtr: %p\n", ptrToPtr);   // Output: 10

     printf("Value of address of &ptrToPtr: %p\n", &ptrToPtr);   // Output: 10
    printf("Value of address of &ptr: %p\n", &ptr);   // Output: 10



    modifyPointer(ptrToPtr);


    printf("Value of data after modification: %d\n", data);                 // Output: 20
    printf("Value of pointer *ptr after modification: %d\n", *ptr);         // Output: 20
    printf("Value of pointer **ptrToPtr after modification: %d\n", **ptrToPtr); // Output: 20

    printf("Value of pointer ptr: %p\n", ptr);               // Output: 10
    printf("Value of pointer *ptrToPtr: %p\n", *ptrToPtr);   // Output: 10


    return 0;
}