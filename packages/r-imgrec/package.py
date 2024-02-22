# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImgrec(RPackage):
	"""An Interface for Image Recognition

	Provides an interface for image recognition using the 'Google Vision API' <https://cloud.google.com/vision/> .  Converts API data for features such as object detection and optical character recognition to data frames. The package also includes functions for analyzing image annotations.
	"""
	
	homepage = "https://github.com/cschwem2er/imgrec"
	cran = "imgrec" 

	version("0.1.3", md5="5d92d104dafcce85a03efd60ac30f7ef")

	depends_on("r-knitr@1.3:", type=("build", "run"))
	depends_on("r-base64enc@0.1.0:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
