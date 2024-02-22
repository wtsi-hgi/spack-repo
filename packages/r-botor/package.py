# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBotor(RPackage):
	"""'AWS Python SDK' ('boto3') for R

	Fork-safe, raw access to the 'Amazon Web Services' ('AWS') 'SDK' via the 'boto3' 'Python' module, and convenient helper functions to query the 'Simple Storage Service' ('S3') and 'Key Management Service' ('KMS'), partial support for 'IAM', the 'Systems Manager Parameter Store' and 'Secrets Manager'.
	"""
	
	homepage = "https://daroczig.github.io/botor/"
	cran = "botor" 

	version("0.4.0", md5="85807fb1f0427dca9f55492c4863b496")

	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
