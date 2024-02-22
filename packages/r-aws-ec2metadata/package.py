# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsEc2metadata(RPackage):
	"""Get EC2 Instance Metadata

	Retrieve Amazon EC2 instance metadata from within the running instance.
	"""
	
	homepage = "https://github.com/cloudyr/aws.ec2metadata"
	cran = "aws.ec2metadata" 

	version("0.2.0", md5="a6c3cdfe1d40249ebabdc286395f9cfa")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
