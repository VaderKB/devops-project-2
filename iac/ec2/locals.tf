locals {
  instance_type_val = var.ENV == "dev" ? "t2.medium" : "m5.large"
}