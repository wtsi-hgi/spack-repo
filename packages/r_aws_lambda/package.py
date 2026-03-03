# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsLambda(RPackage):
	"""AWS Lambda Client Package

	A simple client package for the Amazon Web Services ('AWS') Lambda 
    API <https://aws.amazon.com/lambda/>.
	"""
	
	homepage = "https://github.com/cloudyr/aws.lambda"
	cran = "aws.lambda" 

	version("0.2.0", md5="86d9f9c9a955d1ddcda08b9c5e36a88a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-aws-signature@0.3.4:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
