# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTehtuner(RPackage):
	"""Fit and Tune Models to Detect Treatment Effect Heterogeneity

	Implements methods to fit Virtual Twins models (Foster et al. 
  (2011) <doi:10.1002/sim.4322>) for identifying subgroups with differential
  effects in the context of clinical trials while controlling the probability
  of falsely detecting a differential effect when the conditional average
  treatment effect is uniform across the study population using parameter
  selection methods proposed in Wolf et al. (2022) 
  <doi:10.1177/17407745221095855>.
	"""
	
	homepage = "https://github.com/jackmwolf/tehtuner"
	cran = "tehtuner" 

	version("0.3.0", md5="db513c039ba31999f539094cf6ec557d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-randomforestsrc", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
