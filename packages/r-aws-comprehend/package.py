# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsComprehend(RPackage):
	"""Client for 'AWS Comprehend'

	Client for 'AWS Comprehend' <https://aws.amazon.com/comprehend>, a cloud natural language processing service that can perform a number of quantitative text analyses, including language detection, sentiment analysis, and feature extraction.
	"""
	
	homepage = "https://github.com/cloudyr/aws.comprehend"
	cran = "aws.comprehend" 

	version("0.2.1", md5="5e9049ea2fa3ddc2fa899a454fb39ef2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-aws-signature@0.3.4:", type=("build", "run"))
