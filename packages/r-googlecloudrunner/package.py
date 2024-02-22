# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGooglecloudrunner(RPackage):
	"""R Scripts in the Google Cloud via Cloud Run, Cloud Build and
Cloud Scheduler

	Tools to easily enable R scripts in the Google Cloud Platform.
  Utilise cloud services such as Cloud Run <https://cloud.google.com/run/> for R 
  over HTTP, Cloud Build <https://cloud.google.com/build> for Continuous 
  Delivery and Integration services and 
  Cloud Scheduler <https://cloud.google.com/scheduler/> for scheduled scripts.
	"""
	
	homepage = "https://code.markedmondson.me/googleCloudRunner/"
	cran = "googleCloudRunner" 

	version("0.5.0", md5="6d0b78236c4607fef2d1db83f24bc470")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-cli@2.0.2:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-googleauthr@2:", type=("build", "run"))
	depends_on("r-googlecloudstorager@0.7:", type=("build", "run"))
	depends_on("r-googlepubsubr@0.0.2:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-jose@1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-openssl@1.4.1:", type=("build", "run"))
	depends_on("r-plumber@1:", type=("build", "run"))
	depends_on("r-usethis@1.6:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml@2.2:", type=("build", "run"))
