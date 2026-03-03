# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsS3(RPackage):
	"""'AWS S3' Client Package

	A simple client package for the Amazon Web Services ('AWS') Simple
    Storage Service ('S3') 'REST' 'API' <https://aws.amazon.com/s3/>.
	"""
	
	homepage = "https://github.com/cloudyr/aws.s3"
	cran = "aws.s3" 

	version("0.3.21", md5="2b63f4deda38d33076486cb74bed9581", url="https://cran.r-project.org/src/contrib/aws.s3_0.3.21.tar.gz")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2@1:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-aws-signature@0.3.7:", type=("build", "run"))
