<?php
    $url = 'http://127.0.0.1:8080/predict';
    $data = array('data' => $_POST['data']);

    $options = array(
        'http' => array(
            'header'  => "Content-type: application/json\r\n",
            'method'  => 'POST',
            'content' => json_encode($data)
        )
    );

    $context  = stream_context_create($options);
    $response = file_get_contents($url, false, $context);
    $result = json_decode($response, true);
    echo $result['prediction'];
?>