# 🛡️ Bootcamp A1 - Cybersecurity & Network Analysis Training

مستودع تقني شامل لتوثيق التكاليف العملية، المشاريع البرمجية، والتطبيقات الأمنية المنجزة ضمن **مخيم التدريب المكثف للأمن السيبراني وتحليل الشبكات (22 أسبوعاً / 415 ساعة)**، بتنظيم من **شركة A1 للاستشارات** و**مركز ألتمت للتدريب والاستشارات** في صنعاء.

---

## 🗺️ نظرة عامة على المسار التدريبي

ينقسم البرنامج التدريبي إلى ثلاث مراحل متكاملة لبناء المهارات من التأسيس البرمجي وحتى التطبيق الأمني المتقدم:

* **المرحلة الأولى (التأسيسية - أونلاين):** بناء الأساس البرمجي القوي وتطوير الأدوات الأمنية من الصفر باستخدام لغات (C, Python, PHP, JavaScript).
* **المرحلة الثانية (التخصصية - حضوري):** التعمق في اختبار الاختراق، أمن الشبكات، تحليل السجلات والتهديدات (SOC)، والهندسة العكسية للبرمجيات الخبيثة.
* **المرحلة الثالثة (المشاريع التقييمية):** تنفيذ مشاريع تخرج تطبيقية تحاكي بيئات العمل الحقيقية بإشراف خبراء المجال.

---

## 📂 هيكلية المستودع (Repository Structure)

تنظيم الملفات والمشاريع المنجزة في المرحلة التأسيسية (`Foundation-Stage-Costs`):

```text
Foundation-Stage-Costs/
├── 📁 Assignment Day1/                  # فحص قوة كلمات المرور بلغة C
│   └── 📄 Password_Check.c
├── 📁 Assignment Day3 - Hxe&log/        # عارض الملفات السداسية ومحلل السجلات
│   ├── 📄 README.md
│   ├── 📁 Hex-viewe/
│   │   └── 📄 hex_view.c
│   └── 📁 Log_check/
│       └── 📄 log.c
├── 📁 Assignment-5-Port-Scanner/        # أداة فحص المنافذ المتعددة (Multithreaded)
│   └── 📄 port_scanner.py
├── 📁 Assignment-6-Banner-Grabbing/     # أداة استخراج معلومات الخدمات (Banner Grabbing)
│   └── 📄 banner_grabber.py
├── 📁 Assignment-7-Log-Analyzer/        # محلل سجلات الخوادم الآلي
│   ├── 📄 access.log
│   └── 📄 log_analyzer.py
├── 📁 Assignment-8-Password-Hasher/     # مولد كلمات المرور والتشفير باستخدام SHA-256
│   └── 📄 password_hasher.py
├── 📁 Assignment-9-File-Integrity/      # نظام مراقبة سلامة الملفات (FIM)
│   ├── 📄 baseline.sha256
│   ├── 📄 fim_alerts.log
│   ├── 📄 fim_monitor.py
│   └── 📄 sensitive_config.conf
├── 📁 Assignment-10-REST-API/           # بناء واجهة برمجة تطبيقات (REST API)
│   ├── 📄 api.php
│   └── 📄 index.html
├── 📁 Assignment-11-SQLi-Defense/       # الحماية من ثغرات حقن قواعد البيانات (SQLi)
│   ├── 📄 index.html
│   └── 📄 search.php
├── 📁 Assignment-12-Secure-Upload/      # نظام رفع الملفات الآمن والتحقق من النوع (MIME)
│   ├── 📄 index.html
│   ├── 📄 upload.php
│   ├── 📁 test_samples/
│   └── 📁 uploads/
├── 📁 Assignment-13-Session-Security/   # تأمين الجلسات وملفات تعريف الارتباط (Cookies)
│   ├── 📄 index.html
│   └── 📄 session_manager.php
└── 📁 Assignment-14-DOM-XSS/            # الحماية من ثغرات DOM-Based XSS
    ├── 📄 index.html
    └── 📄 script.js
```

---

## 📊 سجل المهام والتكاليف المنجزة (Progress Tracker)

> يتم تحديث هذا الجدول دورياً لتتبع التقدم وإضافة المشاريع الجديدة في المخيم.

| التكليف | اسم المشروع / المهمة | التقنيات والمفاهيم المستخدمة | المجلد | الحالة |
| :--- | :--- | :--- | :--- | :---: |
| **Day 1** | **Password Strength Checker** | C (`Strings`, `ctype.h`) | `Assignment Day1` | ✅ مكتمل |
| **Day 3 (A)** | **Hexadecimal File Viewer** | C (`Binary Files`, `File I/O`) | `Hex-viewe` | ✅ مكتمل |
| **Day 3 (B)** | **SOC Log File Parser** | C (`File Parsing`, `String Search`) | `Log_check` | ✅ مكتمل |
| **Task 5** | **Multithreaded TCP Port Scanner** | Python (`socket`, `ThreadPoolExecutor`) | `Assignment-5-Port-Scanner` | ✅ مكتمل |
| **Task 6** | **Service Banner Grabbing Tool** | Python (`socket`, `TCP/HTTP`) | `Assignment-6-Banner-Grabbing` | ✅ مكتمل |
| **Task 7** | **Automated Web Log Analyzer** | Python (`Regex`, `Log Analysis`) | `Assignment-7-Log-Analyzer` | ✅ مكتمل |
| **Task 8** | **Password Generator & Hasher** | Python (`secrets`, `hashlib` SHA-256) | `Assignment-8-Password-Hasher` | ✅ مكتمل |
| **Task 9** | **File Integrity Monitoring (FIM)** | Python (`SHA-256`, `File Monitoring`) | `Assignment-9-File-Integrity` | ✅ مكتمل |
| **Task 10** | **HTTP RESTful API** | PHP (`HTTP Methods`, `JSON`) | `Assignment-10-REST-API` | ✅ مكتمل |
| **Task 11** | **SQL Injection (SQLi) Defense** | PHP (`PDO`, `Prepared Statements`) | `Assignment-11-SQLi-Defense` | ✅ مكتمل |
| **Task 12** | **Secure File Upload System** | PHP (`MIME Validation`, `Fileinfo`) | `Assignment-12-Secure-Upload` | ✅ مكتمل |
| **Task 13** | **Session & Cookie Security** | PHP (`Sessions`, `HttpOnly`, `SameSite`) | `Assignment-13-Session-Security` | ✅ مكتمل |
| **Task 14** | **DOM-Based XSS Prevention** | HTML, JS (`DOM`, `textContent`) | `Assignment-14-DOM-XSS` | ✅ مكتمل |

---

## 🛠️ المهارات والأدوات التقنية (Tech Stack)

* **لغات البرمجة:** C, Python, PHP, JavaScript (ES6+).
* **تطوير وتأمين الويب:** HTML5, CSS3, DOM Manipulation, REST APIs, Secure Coding Practices.
* **المفاهيم والأدوات الأمنية المنفذة:**
  * تحليل السجلات واكتشاف الأنماط المشبوهة (Log Parsing & Analysis).
  * فحص الشبكات واستكشاف الخدمات (Port Scanning & Banner Grabbing).
  * مراقبة سلامة الملفات والتشفير التطبيقي (FIM & Cryptographic Hashing).
  * سد الثغرات الشائعة في تطبيقات الويب (SQLi, XSS, Insecure File Upload, Session Hijacking).
* **بيئة التطوير والتشغيل:** Windows, Command Prompt / PowerShell, GCC Compiler, Python 3, XAMPP (Apache), Git & GitHub.

---

**إعداد وتنفيذ المتدرب:** *أسامه مهدي الخطري*
