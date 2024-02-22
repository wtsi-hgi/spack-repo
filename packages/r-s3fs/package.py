# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS3fs(RPackage):
	"""'Amazon Web Service S3' File System

	Access 'Amazon Web Service Simple Storage Service' ('S3') <https://aws.amazon.com/s3/>
    as if it were a file system. Interface based on the R package 'fs'.
	"""
	
	homepage = "https://github.com/DyfanJones/s3fs"
	cran = "s3fs" 

	version("0.1.4", md5="b52ebd145c42c25221bb6c81aa2a9106")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-paws-storage@0.2:", type=("build", "run"))
