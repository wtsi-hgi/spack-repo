# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoreparty(RPackage):
	"""A Toolbox for Conditional Inference Trees and Random Forests

	Additions to 'party' and 'partykit' packages : tools for the interpretation of forests (surrogate trees, prototypes, etc.), feature selection (see Gregorutti et al (2017) <arXiv:1310.5726>, Hapfelmeier and Ulm (2013) <doi:10.1016/j.csda.2012.09.020>, Altmann et al (2010) <doi:10.1093/bioinformatics/btq134>) and parallelized versions of conditional forest and variable importance functions. Also modules and a shiny app for conditional inference trees.
	"""
	
	cran = "moreparty" 

	version("0.4", md5="1f05033973563def1eebdd45fe8baab9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-varimp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-measures", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-iml", type=("build", "run"))
	depends_on("r-pdp", type=("build", "run"))
	depends_on("r-vip@0.4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-rclipboard", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-datamods", type=("build", "run"))
	depends_on("r-phosphoricons", type=("build", "run"))
