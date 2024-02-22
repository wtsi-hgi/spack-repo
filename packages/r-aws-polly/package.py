# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsPolly(RPackage):
	"""Client for AWS Polly

	A client for AWS Polly <http://aws.amazon.com/documentation/polly>, a speech synthesis service.
	"""
	
	homepage = "https://github.com/cloudyr/aws.polly"
	cran = "aws.polly" 

	version("0.1.5", md5="c35750aa878b5590f312247fffd6a8b6")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-aws-signature@0.3.4:", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
