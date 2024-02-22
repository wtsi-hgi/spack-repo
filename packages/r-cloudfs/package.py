# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCloudfs(RPackage):
	"""Streamlined Interface to Interact with Cloud Storage Platforms

	A unified interface for simplifying cloud storage interactions, 
    including uploading, downloading, reading, and writing files, with functions
    for both 'Google Drive' (<https://www.google.com/drive/>) and 'Amazon S3' 
    (<https://aws.amazon.com/s3/>).
	"""
	
	homepage = "https://g6t.github.io/cloudfs/"
	cran = "cloudfs" 

	version("0.1.2", md5="cb0e9fc82c0e1d06f08324db3d32ad99")

	depends_on("r-aws-s3", type=("build", "run"))
	depends_on("r-googledrive", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
