#include <stdio.h>
#include <string.h>


int main (){

    char password[100];


    int has_upper =0;
    int has_lower =0;
    int has_digit =0;
    int has_symbol =0;
    int has_length =0;

    printf ("please enter the password to check:  ");

    fgets (password,sizeof(password), stdin);
    

    int length =strlen(password);

    if (length > 8) has_length =1;

    for (int i = 0 ; i < length ; i++ ){

        char ch = password[i];

        if (ch >= 'A' && ch <= 'Z'){
            has_upper = 1 ;
        }else if (ch >= 'a' && ch <= 'z'){
            has_lower = 1 ;
        }else if (ch >= '0' && ch <= '9'){
            has_digit = 1 ;
        }else if (ch != ' ' && ch != '\t'){
            has_symbol = 1 ;
        }
    }

    // استخدمت شرط %c ؟ Y or N  الذي يعمل مثل الشرط  else if
    
    printf("\n [%c] length > 8 \n", has_length ? 'y' : 'n');
    printf(" [%c] upper > (A-Z)\n", has_upper ? 'y' : 'n');
    printf(" [%c] lower (a-z)\n", has_lower ? 'y' : 'n');
    printf(" [%c] digit  (1-9)\n", has_digit ? 'y' : 'n');
    printf(" [%c] symbols   \n", has_symbol ? 'y' : 'n');

    if (has_length && has_upper && has_lower && has_digit && has_symbol){
        printf(" PASS (Strong) \n");
    } else {
        printf("FAIL (Weak) \n");
    }

    return 0;
}