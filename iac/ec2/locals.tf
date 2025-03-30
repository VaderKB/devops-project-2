locals {
  instance_type_val = var.env == "dev" ? "t2.medium" : "m5.large"
}