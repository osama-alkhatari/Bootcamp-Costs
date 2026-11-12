<?php
header("Content-Type: application/json; charset=UTF-8");

// بيانات اختبارية ثابتة غير قابلة للتعديل أثناء التشغيل
const SEED_USERS = [
    ["admin", "Administrator", "admin@sec.local"],
    ["ahmed", "SOC Analyst", "ahmed@sec.local"],
    ["sara", "Pentester", "sara@sec.local"]
];

try {
    // تهيئة قاعدة بيانات SQLite 
    $pdo = new PDO("sqlite::memory:", null, null, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES => false
    ]);

    // إنشاء جدول المستخدمين وإدراج السجلات التجريبية
    $pdo->exec("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, role TEXT, email TEXT)");
    $stmt = $pdo->prepare("INSERT INTO users (username, role, email) VALUES (?, ?, ?)");
    foreach (SEED_USERS as $u) {
        $stmt->execute($u);
    }

    $username = $_GET['username'] ?? '';
    $mode = $_GET['mode'] ?? 'secure';

    if ($mode === 'vulnerable') {
        // الطريقة غير الآمنة: دمج المدخل مباشرة داخل نص الاستعلام (عرضة لـ SQLi)
        $query = "SELECT * FROM users WHERE username = '$username'";
        $rows = $pdo->query($query)->fetchAll();
        $note = "VULNERABLE: Direct string concatenation allows SQL Injection bypass.";
    } else {
        // الطريقة الآمنة: استخدام (pdo)
        $query = "SELECT * FROM users WHERE username = :username";
        $stmt = $pdo->prepare($query);
        $stmt->execute([':username' => $username]);
        $rows = $stmt->fetchAll();
        $note = "SECURE (PDO Prepared): Input bound strictly as literal parameter. SQLi blocked.";
    }

    echo json_encode([
        "mode" => $mode,
        "input" => $username,
        "query" => $query,
        "security_note" => $note,
        "count" => count($rows),
        "results" => $rows
    ], JSON_PRETTY_PRINT) . "\n";

} catch (PDOException $e) {
    http_response_code(400);
    echo json_encode([
        "mode" => $mode ?? 'unknown',
        "error" => "Query execution rejected safely without leaking schema details."
    ], JSON_PRETTY_PRINT) . "\n";
}
