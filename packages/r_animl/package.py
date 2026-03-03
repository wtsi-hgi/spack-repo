# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAniml(RPackage):
	"""A Collection of ML Tools for Conservation Research

	Functions required to classify subjects within camera trap field data. The package can handle both images and videos. The authors recommend a two-step approach using Microsoft's 'MegaDector' model and then a second model trained on the classes of interest.
	"""
	
	cran = "animl" 

	version("1.1.0", md5="3b651aa089d9bcd7b029e9109e65faf4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tensorflow@2.5:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-tfdatasets", type=("build", "run"))
	depends_on("r-exifr", type=("build", "run"))
	depends_on("r-av", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
