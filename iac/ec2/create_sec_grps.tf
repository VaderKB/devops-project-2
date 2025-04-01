resource "aws_security_group" "ec2_sec_grp" {

  name = "${var.ENV}-firewall-rules"

}

resource "aws_vpc_security_group_ingress_rule" "allow_tls_ipv4" {
  for_each          = var.ec2_ports
  security_group_id = aws_security_group.ec2_sec_grp.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = each.value
  ip_protocol       = "tcp"
  to_port           = each.value
}
