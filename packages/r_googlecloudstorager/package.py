# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGooglecloudstorager(RPackage):
	"""Interface with Google Cloud Storage API

	Interact with Google Cloud Storage <https://cloud.google.com/storage/> 
  API in R. Part of the 'cloudyr' <https://cloudyr.github.io/> project.
	"""
	
	homepage = "https://code.markedmondson.me/googleCloudStorageR/"
	cran = "googleCloudStorageR" 

	version("0.7.0", md5="6fd04d13ed0ff9f3872d8f75aa8c7b33")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-googleauthr@1.4:", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-jsonlite@1:", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-zip@2.0.3:", type=("build", "run"))
