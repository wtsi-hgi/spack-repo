# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapscanner(RPackage):
	"""Print Maps, Draw on Them, Scan Them Back in

	Enables preparation of maps to be printed and drawn on.
    Modified maps can then be scanned back in, and hand-drawn marks
    converted to spatial objects.
	"""
	
	homepage = "https://github.com/ropensci/mapscanner"
	cran = "mapscanner" 

	version("0.0.6", md5="5a31b5f07b10e523c349f7467f61cdd5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reproj", type=("build", "run"))
	depends_on("r-rniftyreg", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-slippymath", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
