# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHesim(RPackage):
	"""Health Economic Simulation Modeling and Decision Analysis

	A modular and computationally efficient R package for  
  parameterizing, simulating, and analyzing health economic simulation 
  models. The package supports cohort discrete time state transition models 
  (Briggs et al. 1998) <doi:10.2165/00019053-199813040-00003>,
  N-state partitioned survival models (Glasziou et al. 1990)
  <doi:10.1002/sim.4780091106>, and individual-level continuous 
  time state transition models (Siebert et al. 2012) <doi:10.1016/j.jval.2012.06.014>,
  encompassing both Markov (time-homogeneous and time-inhomogeneous) and 
  semi-Markov processes. Decision uncertainty from a cost-effectiveness analysis is 
  quantified with standard graphical and tabular summaries of a probabilistic 
  sensitivity analysis (Claxton et al. 2005, Barton et al. 2008) <doi:10.1002/hec.985>, 
  <doi:10.1111/j.1524-4733.2008.00358.x>. Use of C++ and data.table
  make individual-patient simulation, probabilistic sensitivity analysis, 
  and incorporation of patient heterogeneity fast.
	"""
	
	homepage = "https://hesim-dev.github.io/hesim/"
	cran = "hesim" 

	version("0.5.4", md5="e49578f05ab04a5d42b59fbece80ed72")
	version("0.5.3", md5="bd6f92446c90a356ea380b92eb5db7ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
