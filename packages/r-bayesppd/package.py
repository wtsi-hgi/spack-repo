# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesppd(RPackage):
	"""Bayesian Power Prior Design

	Bayesian power/type I error calculation and model fitting using 
  the power prior and the normalized power prior for generalized linear models.
  Detailed examples of applying the package are available at <doi:10.32614/RJ-2023-016>. 
  The Bayesian clinical trial design methodology is described in Chen et al. (2011) 
  <doi:10.1111/j.1541-0420.2011.01561.x>, and Psioda and Ibrahim (2019) 
  <doi:10.1093/biostatistics/kxy009>. The normalized power prior is described in Duan et al. (2006) 
  <doi:10.1002/env.752> and Ibrahim et al. (2015) <doi:10.1002/sim.6728>. 
	"""
	
	cran = "BayesPPD" 

	version("1.1.2", md5="78714aaf0ab1a27013350ff9bb52b06c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
