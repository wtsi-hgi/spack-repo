# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtrreg(RPackage):
	"""DTR Estimation and Inference via G-Estimation, Dynamic WOLS,
Q-Learning, and Dynamic Weighted Survival Modeling (DWSurv)

	Dynamic treatment regime estimation and inference via G-estimation, 
  dynamic weighted ordinary least squares (dWOLS) and Q-learning. Inference via 
  bootstrap and recursive sandwich estimation. Estimation and 
  inference for survival outcomes via Dynamic Weighted Survival Modeling (DWSurv). 
  Extension to continuous treatment variables. Wallace et al. (2017) 
  <DOI:10.18637/jss.v080.i02>; Simoneau et al. (2020) 
  <DOI:10.1080/00949655.2020.1793341>.
	"""
	
	cran = "DTRreg" 

	version("2.1", md5="d878bba66415dd0b8e520002a2de0421")
	version("2.2", md5="21d02e4907f85564b7ca15e06ebb43af")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
