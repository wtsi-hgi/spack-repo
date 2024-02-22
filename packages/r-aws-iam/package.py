# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsIam(RPackage):
	"""AWS IAM Client Package

	A simple client for the Amazon Web Services ('AWS') Identity
    and Access Management ('IAM') 'API' <https://aws.amazon.com/iam/>.
	"""
	
	homepage = "https://github.com/cloudyr/aws.iam"
	cran = "aws.iam" 

	version("0.1.8", md5="48c5a6e4904c3f32e41dbd7b96800d03")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-aws-signature@0.3.4:", type=("build", "run"))
