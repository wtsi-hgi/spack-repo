# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbnmatime(RPackage):
	"""Run Time-Course Model-Based Network Meta-Analysis (MBNMA) Models

	Fits Bayesian time-course models for model-based network meta-analysis (MBNMA) that allows inclusion of multiple
  time-points from studies. Repeated measures over time are accounted for within studies by applying different time-course functions,
  following the method of Pedder et al. (2019) <doi:10.1002/jrsm.1351>. 
  The method allows synthesis of studies with multiple follow-up measurements that can account for time-course for a single or multiple 
  treatment comparisons. Several general time-course functions are provided; others may be added 
  by the user. Various characteristics can be flexibly added to the models, such as correlation between time points and shared 
  class effects. The consistency of direct and indirect evidence in the network can be assessed using unrelated mean effects 
  models and/or by node-splitting.
	"""
	
	homepage = "https://hugaped.github.io/MBNMAtime/"
	cran = "MBNMAtime" 

	version("0.2.4", md5="4c9c33a4f32f7b392f6f8c485bd2139d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-r2jags@0.5.7:", type=("build", "run"))
	depends_on("r-rjags@4.8:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-checkmate@1.8.5:", type=("build", "run"))
	depends_on("r-rdpack@0.10.1:", type=("build", "run"))
	depends_on("jags@4.3.0:", type=("build", "link", "run"))
