<?php
header("Content-Type: application/json; charset=UTF-8");

// سياسة كوكيز ثابتة غير قابلة للتعديل أثناء التشغيل
const STRICT_COOKIE_POLICY = [
    'lifetime' => 3600,
    'path'     => '/',
    'httponly' => true,
    'samesite' => 'Strict'
];

$isHttps = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off');

// 1. تفعيل الوضع الصارم للجلسات وضبط خصائص الكوكي قبل البدء
ini_set('session.use_strict_mode', '1');
session_set_cookie_params(array_merge(STRICT_COOKIE_POLICY, ['secure' => $isHttps]));

session_start();

// 2. إصدار كوكي محمية بخصائص مصفوفة الخيارات 
setcookie('protected_cookie', 'SECRET_SESSION_BADGE_99', [
    'expires'  => time() + 3600,
    'path'     => '/',
    'secure'   => $isHttps,
    'httponly' => true,
    'samesite' => 'Strict'
]);

// كوكي عادية غير محمية للمقارنة العملية عند فحص 
setcookie('public_cookie', 'theme_dark', [
    'expires'  => time() + 3600,
    'path'     => '/',
    'secure'   => false,
    'httponly' => false,
    'samesite' => 'Lax'
]);

$action = $_REQUEST['action'] ?? 'status';
$oldId = session_id();

// 3. تجديد معرف الجلسة بعد تسجيل الدخول لمنع Session Fixation
if ($action === 'login') {
    session_regenerate_id(true);
    $_SESSION['user'] = $_REQUEST['username'] ?? 'cyber_admin';
    $_SESSION['logged_in'] = true;
}

echo json_encode([
    "action" => $action,
    "user" => $_SESSION['user'] ?? 'guest',
    "old_session_id" => $oldId,
    "current_session_id" => session_id(),
    "session_regenerated" => ($oldId !== session_id()),
    "set_cookie_headers" => array_values(array_filter(headers_list(), fn($h) => stripos($h, 'Set-Cookie:') === 0))
], JSON_PRETTY_PRINT) . "\n";
