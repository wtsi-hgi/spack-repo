# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGimme(RPackage):
	"""Group Iterative Multiple Model Estimation

	Data-driven approach for arriving at person-specific time series models. The method first identifies which relations replicate across the majority of individuals to detect signal from noise. These group-level relations are then used as a foundation for starting the search for person-specific (or individual-level) relations. See Gates & Molenaar (2012) <doi:10.1016/j.neuroimage.2012.06.026>. 
	"""
	
	homepage = "https://github.com/GatesLab/gimme/"
	cran = "gimme" 

	version("0.7-16", md5="a85ddba210fe85c40ef2473945b1727c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lavaan@0.6.17:", type=("build", "run"))
	depends_on("r-igraph@1.0.0:", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-miivsem@0.5.4:", type=("build", "run"))
	depends_on("r-imputets@3:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
