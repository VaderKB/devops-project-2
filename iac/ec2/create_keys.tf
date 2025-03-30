resource "tls_private_key" "rsa_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "local_file" "save_private_key" {
  content  = tls_private_key.rsa_key.private_key_openssh
  filename = "${var.env}-my-key.pem"
}

resource "aws_key_pair" "ec2_key" {
  key_name   = "${var.env}-ec-key-pair"
  public_key = tls_private_key.rsa_key.public_key_openssh
}