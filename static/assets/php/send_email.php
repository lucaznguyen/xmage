<?php
if (isset($_POST['email']) && !empty($_POST['email'])) {
  $subject = "New contact request: $_POST['name']";
  $message = $_POST['message'];
  $headers = 'From: lucaznguyenofficial@gmail.com' . "\r\n" .
             'Reply-To: ' . $_POST['email']. "\r\n" .
             'X-Mailer: PHP/' . phpversion();

  mail('lucaznguyenofficial@gmail.com', $subject, $message, $headers);

  die('Thank you for your email');
}