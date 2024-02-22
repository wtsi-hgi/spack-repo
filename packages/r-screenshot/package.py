# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScreenshot(RPackage):
	"""Take Screenshots (Screen Capture) from R Command

	Take screenshots from R command and locate an image position.
	"""
	
	homepage = "https://github.com/matutosi/screenshot"
	cran = "screenshot" 

	version("0.9.0", md5="9f6ae49caae7654341c198936edda469")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
