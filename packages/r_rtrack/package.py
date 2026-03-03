# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtrack(RPackage):
	"""Spatial Navigation Strategy Analysis

	A toolkit for the analysis of paths from spatial tracking experiments and calculation of goal-finding strategies. 
    This package is centered on an approach using machine learning for path classification.
	"""
	
	homepage = "https://rupertoverall.net/Rtrack/"
	cran = "Rtrack" 

	version("2.0.3", md5="9b335228858d9210f65cad57208feba7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
