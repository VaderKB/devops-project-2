resource "aws_instance" "myec2" {
  ami           = "ami-05b10e08d247fb927"
  instance_type = local.instance_type_val
  tags = {
    Name = "${ var.EC2_NAME }-ec2"
  }
  vpc_security_group_ids = [aws_security_group.ec2_sec_grp.id]
  key_name               = aws_key_pair.ec2_key.key_name
}
