# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsSignature(RPackage):
	"""Amazon Web Services Request Signatures

	Generates version 2 and version 4 request signatures for Amazon Web Services ('AWS') <https://aws.amazon.com/> Application Programming Interfaces ('APIs') and provides a mechanism for retrieving credentials from environment variables, 'AWS' credentials files, and 'EC2' instance metadata. For use on 'EC2' instances, users will need to install the suggested package 'aws.ec2metadata' <https://cran.r-project.org/package=aws.ec2metadata>.
	"""
	
	homepage = "https://github.com/cloudyr/aws.signature"
	cran = "aws.signature" 

	version("0.6.0", md5="b8ae2a848fd802e6a582fe1a01149c0b")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
