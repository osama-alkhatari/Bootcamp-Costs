#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    
    if (argc != 3) {
        printf("Usage: %s <logfile> <keyword>\n", argv[0]);
        return 1;
    }

    char *filename = argv[1];
    char *keyword = argv[2];

    // فتح الملف في وضع القراءة
    FILE *f = fopen(filename, "r");
    if (f == NULL) {
        printf("Error: Can't open file %s\n", filename);
        return 1;
    }

    char line[512];
    int line_num = 0;
    int alerts = 0;

    printf("[*] Scanning file: %s for keyword: '%s'...\n\n", filename, keyword);


    while (fgets(line, sizeof(line), f) != NULL) {
        line_num++;
        
        if (strstr(line, keyword) != NULL) {
            alerts++;
            
            size_t len = strlen(line);
            if (len > 0 && line[len-1] == '\n') {
                line[len-1] = '\0';
            }
            
            printf("[!] Alert Line %d: %s\n", line_num, line);
        }
    }

    fclose(f);

    
    printf("\n=== Scanning Done ===\n");
    printf("Total Lines Scanned: %d\n", line_num);
    printf("Total Alerts Found : %d\n", alerts);

    if (alerts == 0) {
        printf("[+] Clean: No suspicious activities found.\n");
    }

    return 0;
}
