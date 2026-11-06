#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    FILE *f = fopen(argv[1], "rb");
    if (f == NULL) {
        printf("Error: Can't open file %s\n", argv[1]);
        return 1;
    }

    unsigned char buf[16];
    size_t bytes_read;
    unsigned int offset = 0;

    while ((bytes_read = fread(buf, 1, 16, f)) > 0) {
        
        printf("%08X  ", offset);

        // طباعة البايتات بصيغة Hexa
        for (int i = 0; i < 16; i++) {
            if (i < bytes_read) {
                printf("%02X ", buf[i]);
            } else {
                printf("   "); 
            }
            
            if (i == 7) {
                printf(" ");
            }
        }

        printf(" | ");

        // طباعة الأحرف  ASCII 
        for (int i = 0; i < bytes_read; i++) {
            if (buf[i] >= 32 && buf[i] <= 126) {
                printf("%c", buf[i]);
            } else {
                printf(".");
            }
        }

        printf("\n");
        offset += bytes_read; // تحديث الموقع الذي بعده
    }

    fclose(f);
    return 0;
}