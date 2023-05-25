### programming
#### Basics
1. A computer has mainly three important components
   
   a. storage , namely ram, hardisk etc.
   b. processing device namely cpu
   c. display devices namely monitor

2. IDE : Integrated development editor : vscode, atom,vim etc.
3. The program starts executing from the main function.
4. Execution of a program happens in a sequential manner.
5. assigned variables are stored in ram.
6. Naming Rules of variables

    a. only consists of letters, digits and underscores
    b. first letter : proper letter / under_score
    c. no reserved keywords, no intermittent spaces
    d. casing matters

7. bit is the smallest unit of memory
8. 1 byte is 8 bits
9. Integer value takes 4 bytes memory in ram.
10. implicit type casting is based on the data type defined
11. explicit type casting where we express our will to change the type.
12. American standard code for information interchange (ASCII)
13. precision: 6 digits after decimal, rounded off till 1st 6 digits of decimal.
14. for float , 4 bytes are allocated, double 8 bytes
15. Format specifier is used to specify the datatype of var being printed.
16. Operators are used to do mathematical operations between operands.
17. x+y : + is an operator , x,y are operands.
18. dividend=divisor*quotient + remainder
19. Modulo operator a%b : 17%5=2
20. Rules of evaluating an expression : BODMAS --> precedence rule.
21. If we have operators of equal precedence then we use associativity rules L-> R or R->L
22. post increment > pre increment in precedence.
23. x==y used to check equality.
24. x!=y used to check non equality.
25. Logical operators : and, or not.
26. decision making constructs if , if else.
27. Looping constructs for loop , while loop and do while.
28. Arrays are collection of data.
29. Indexing in an array starts with 0 and not 1.
30. If we try to access an index which is not present in the array , we get index out of bound exception
31. Memory allocation is random and its not contiguos , x what is the memory of address of the list.
32. If we just know the address of first byte block that is enough to get the rest of the addresses of the elements in case of an array.
33.In case of array pointer base address is stored in arr, *(arr+i) ==> arr[i]. 
34,The name of the array is a constant pointer , it doesnot change and we cannot modify this pointer.
35.Pointer to Pointer
36,int a=5 , int*b=&a , int** c=&b , since b is a pointer to int , and in order to store a pointer to int , we need pointer to pointer int.
37. Now in order to print a=5 is print(a, *b,**c)
38. how to create an array of pointers int* pointers[3] and then we can do , x=1, pointers[0]=&x, now to print the value of x we can do *pointers[0]
39.int ages[10] what is the data type of ages ,since ages consists of base address the datatype is int*
38. int* pointers[3] what is the data type of pointers , since it holds a pointer to the pointer to int, its datatype is int**.
39. In a 2d array , every element is in contiguous memory locations.
40. pointers[i][j] =====> *(pointers[i]+j) 
41. Functions are used to avoid code redundancy 
