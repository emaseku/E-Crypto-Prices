output "lambda_function_name" {
  value = aws_lambda_function.crypto_price_puller.function_name
}

output "s3_bucket_name" {
  value = var.s3_bucket_name
}
