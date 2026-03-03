# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtlsdeep(RPackage):
	"""Post-Hurricane Damage Severity Classification from TLS and AI

	Terrestrial laser scanning (TLS) data processing and post-hurricane damage severity classification at the individual tree level using deep Learning. Further details were published in Klauberg et al. (2023) <doi:10.3390/rs15041165>.
	"""
	
	homepage = "https://github.com/carlos-alberto-silva/rTLsDeep"
	cran = "rTLsDeep" 

	version("0.0.5", md5="cd05af0882752751facb2f6560f9aaa3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lidr", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
