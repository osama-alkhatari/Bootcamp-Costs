# Security Tools in C 

مستودع مخصص للتكليفات البرمجية الخاصة بتحليل السجلات وفحص الملفات الثنائية بلغة C لمحللي الـ SOC.

## الأدوات المتاحة:
1. **Log File Parser (log_parser.c)**: أداة لتصفية وفحص السجلات الأمنية سطرًا بسطر والبحث عن الأنشطة المشبوهة دون استهلاك الذاكرة.
2. **Hexadecimal Viewer (hex_viewer.c)**: أداة لعرض قيم البايتات الخام للملفات بصيغة الهكس والـ ASCII لفحص هيدر الملفات والتواقيع الرقمية.

## طريقة التشغيل عبر الـ Terminal:
# بناء وتشغيل أداة السجلات
gcc log.c -o logs
./logs win_secur.txt FAILED

# بناء وتشغيل عارض الهكس
gcc hex_view.c -o hexview
./hexview win_secur.txt
./hexview mylog.txt

