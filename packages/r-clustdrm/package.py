# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustdrm(RPackage):
	"""Clustering Dose-Response Curves and Fitting Appropriate Models
to Them

	Functions to identify the pattern of a dose-response
		curve. Then fit a set of appropriate models to it according to the identified pattern, 
		followed by model averaging to estimate the effective dose.
	"""
	
	cran = "clustDRM" 

	version("0.1-0", md5="1405d9d7647f4399d3ef1c898d5feece")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-orcme", type=("build", "run"))
	depends_on("r-oriclust", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-isogene", type=("build", "run"))
	depends_on("r-dosefinding", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-mcpmod", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
