<?php
header("Content-Type: application/json; charset=UTF-8");

// ثوابت أمنية غير قابلة للتعديل أثناء التشغيل (Immutability)
const MAX_FILE_SIZE = 2 * 1024 * 1024; // 2MB
const WHITELIST = [
    "jpg" => "image/jpeg",
    "png" => "image/png",
    "pdf" => "application/pdf"
];

$uploadDir = __DIR__ . "/uploads/";
if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0755, true);
}

if (!isset($_FILES['uploaded_file']) || $_FILES['uploaded_file']['error'] !== UPLOAD_ERR_OK) {
    http_response_code(400);
    echo json_encode(["status" => "error", "message" => "No valid file uploaded."], JSON_PRETTY_PRINT) . "\n";
    exit;
}

$file = $_FILES['uploaded_file'];
$filename = $file['name'];
$tmpPath = $file['tmp_name'];
$size = $file['size'];

// 1. فحص الحجم الأقصى المسموح
if ($size <= 0 || $size > MAX_FILE_SIZE) {
    http_response_code(400);
    echo json_encode(["status" => "rejected", "layer" => "Size Check", "message" => "File exceeds 2MB limit."], JSON_PRETTY_PRINT) . "\n";
    exit;
}

// 2. التحقق من الامتداد عبر القائمة البيضاء (Whitelist)
$ext = strtolower(pathinfo($filename, PATHINFO_EXTENSION));
if (!array_key_exists($ext, WHITELIST)) {
    http_response_code(403);
    echo json_encode(["status" => "rejected", "layer" => "Extension Whitelist", "message" => "Extension .$ext is not allowed."], JSON_PRETTY_PRINT) . "\n";
    exit;
}

// 3. فحص المحتوى الفعلي للملف (MIME Type) عبر finfo_file
$finfo = finfo_open(FILEINFO_MIME_TYPE);
$realMime = finfo_file($finfo, $tmpPath);


if ($realMime !== WHITELIST[$ext]) {
    http_response_code(403);
    echo json_encode([
        "status" => "rejected",
        "layer" => "MIME Inspection",
        "detected_mime" => $realMime,
        "message" => "Spoofing blocked: Actual MIME ($realMime) does not match .$ext extension."
    ], JSON_PRETTY_PRINT) . "\n";
    exit;
}

// 4. توليد اسم عشوائي آمن ونقل الملف مع قفله بصلاحية قراءة فقط (Read-Only 0444)
$safeName = bin2hex(random_bytes(16)) . "." . $ext;
$dest = $uploadDir . $safeName;

if (move_uploaded_file($tmpPath, $dest)) {
    chmod($dest, 0444);
    echo json_encode([
        "status" => "success",
        "original_name" => basename($filename),
        "saved_as" => $safeName,
        "mime_type" => $realMime,
        "permissions" => "0444 (Read-Only)",
        "message" => "File verified, renamed, and stored safely."
    ], JSON_PRETTY_PRINT) . "\n";
} else {
    http_response_code(500);
    echo json_encode(["status" => "error", "message" => "Failed to move uploaded file."], JSON_PRETTY_PRINT) . "\n";
}
