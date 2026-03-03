# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsKms(RPackage):
	"""'AWS Key Management Service' Client Package

	Client package for the 'AWS Key Management Service' <https://aws.amazon.com/kms/>, a cloud service for managing encryption keys.
	"""
	
	homepage = "https://github.com/cloudyr/aws.kms"
	cran = "aws.kms" 

	version("0.1.4", md5="67d41c1bb14fb5238309c1e1fc720d7c")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-aws-signature@0.4:", type=("build", "run"))
