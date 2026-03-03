# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGooglecloudvisionr(RPackage):
	"""Access to the 'Google Cloud Vision' API for Image Recognition,
OCR and Labeling

	Interact with the 'Google Cloud Vision' <https://cloud.google.com/vision/>
  API in R. Part of the 'cloudyr' <https://cloudyr.github.io/> project.
	"""
	
	cran = "googleCloudVisionR" 

	version("0.2.0", md5="9352ebfb82e897d2b76c89a36a45e254")

	depends_on("r-googleauthr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
