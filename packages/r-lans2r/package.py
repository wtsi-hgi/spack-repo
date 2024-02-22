# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLans2r(RPackage):
	"""Work with Look at NanoSIMS Data in R

	R interface for working with nanometer scale secondary ion mass 
    spectrometry (NanoSIMS) data exported from Look at NanoSIMS. 
	"""
	
	homepage = "https://github.com/KopfLab/lans2r"
	cran = "lans2r" 

	version("1.2.0", md5="6cbb74ee92bf6ab2afbd59dd4f1c14bb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-r-matlab", type=("build", "run"))
