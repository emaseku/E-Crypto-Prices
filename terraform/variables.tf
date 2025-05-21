variable "region" {
  default = "us-east-1"
}

variable "lambda_function_name" {
  default = "cryptoPricePuller"
}

variable "s3_bucket_name" {
  default = "emaseku-s3-covid-bucket"
}
