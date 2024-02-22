# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS3(RPackage):
	"""Download Files from 'AWS S3'

	Download files hosted on 'AWS S3' (Amazon Web Services Simple Storage Service; <https://aws.amazon.com/s3/>) to a local directory based on their URI. Avoid downloading files that are already present locally.  Allow for customization of where to store downloaded files.
	"""
	
	homepage = "https://github.com/geomarker-io/s3"
	cran = "s3" 

	version("1.0.0", md5="948b2e06479836544b7ec7935e8d33c4", url="https://cran.r-project.org/src/contrib/s3_1.0.0.tar.gz")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-aws-signature", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
