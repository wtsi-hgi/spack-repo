# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsEcx(RPackage):
	"""Communicating with AWS EC2 and ECS using AWS REST APIs

	
    Providing the functions for communicating with Amazon Web Services(AWS)
    Elastic Compute Cloud(EC2) and Elastic Container Service(ECS).
    The functions will have the prefix 'ecs_' or 'ec2_' depending on the class 
    of the API. The request will be sent via the REST API and the parameters are
    given by the function argument. The credentials can be set via 'aws_set_credentials'.
    The EC2 documentation can be found at <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html>
    and ECS can be found at <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html>.
	"""
	
	homepage = "https://github.com/Jiefei-Wang/aws.ecx"
	cran = "aws.ecx" 

	version("1.0.5", md5="c5af2c217d342385b70a3c5076159cbb")

	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-aws-signature", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
