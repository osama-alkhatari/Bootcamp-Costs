<?php
// ضبط ترويسة الاستجابة بصيغة JSON
header("Content-Type: application/json; charset=UTF-8");

// قائمة ثابتة غير قابلة للتعديل بالطرق المسموحة
const ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'DELETE'];

$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
$headers = function_exists('getallheaders') ? getallheaders() : [];
$authHeader = $headers['Authorization'] ?? ($headers['authorization'] ?? 'Not Provided');

// قراءة وتحليل بيانات JSON القادمة في جسم الطلب
$rawBody = file_get_contents("php://input");
$inputData = [];

if (!empty(trim($rawBody))) {
    $inputData = json_decode($rawBody, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        http_response_code(400);
        echo json_encode([
            "status" => "error",
            "code" => 400,
            "message" => "Invalid JSON payload format"
        ], JSON_PRETTY_PRINT);
        exit;
    }
}

// معالجة الطلب بناءً على طريقة HTTP
switch ($method) {
    case 'GET':
        http_response_code(200);
        $response = [
            "status" => "success",
            "code" => 200,
            "method" => "GET",
            "auth_header" => $authHeader,
            "message" => "Resource retrieved successfully",
            "data" => ["id" => 1, "service" => "Firewall-01", "state" => "Active"]
        ];
        break;

    case 'POST':
        http_response_code(201);
        $response = [
            "status" => "created",
            "code" => 201,
            "method" => "POST",
            "auth_header" => $authHeader,
            "message" => "New record created successfully",
            "received_data" => $inputData
        ];
        break;

    case 'PUT':
        http_response_code(200);
        $response = [
            "status" => "updated",
            "code" => 200,
            "method" => "PUT",
            "auth_header" => $authHeader,
            "message" => "Resource updated successfully",
            "updated_data" => $inputData
        ];
        break;

    case 'DELETE':
        http_response_code(200);
        $response = [
            "status" => "deleted",
            "code" => 200,
            "method" => "DELETE",
            "message" => "Resource deleted successfully",
            "target_id" => $inputData['id'] ?? ($_GET['id'] ?? 1)
        ];
        break;

    default:
        http_response_code(405);
        $response = [
            "status" => "error",
            "code" => 405,
            "method" => $method,
            "allowed_methods" => ALLOWED_METHODS,
            "message" => "HTTP Method Not Allowed"
        ];
        break;
}

echo json_encode($response, JSON_PRETTY_PRINT) . "\n";
