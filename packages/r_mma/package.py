# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMma(RPackage):
	"""Multiple Mediation Analysis

	Used for general multiple mediation analysis. 
	The analysis method is described in Yu and Li (2022) (ISBN: 9780367365479) "Statistical Methods for Mediation, Confounding and Moderation Analysis Using R and SAS", published by Chapman and Hall/CRC; and Yu et al.(2017) <DOI:10.1016/j.sste.2017.02.001> "Exploring racial disparity in obesity: a mediation analysis considering geo-coded environmental factors", published on Spatial and Spatio-temporal Epidemiology, 21, 13-23.  
	"""
	
	homepage = "https://www.r-project.org"
	cran = "mma" 

	version("10.7-1", md5="5ddf9cdb639e94d96af61a8c78c0a601")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
