# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNphpower(RPackage):
	"""Sample Size Calculation under Non-Proportional Hazards

	Performs combination tests and sample size calculation for 
   fixed design with survival endpoints using combination tests under either
   proportional hazards or non-proportional hazards. The combination tests 
   include maximum weighted log-rank test and projection test. The sample 
   size calculation procedure is very flexible, allowing for user-defined
   hazard ratio function and considering various trial conditions like 
   staggered entry, drop-out etc. Trial simulation function is also provided 
   to facilitate the empirical power calculation. The references for 
   projection test and maximum weighted logrank test include Brendel et al. (2014)
   <doi:10.1111/sjos.12059> and Cheng and He (2021) <arXiv:2110.03833>. The 
   references for sample size calculation under proportional hazard include
   Schoenfeld (1981) <doi:10.1093/biomet/68.1.316> and Freedman (1982) <doi:10.1002/sim.4780010204>.
   The references for calculation under non-proportional hazards include 
   Lakatos (1988) <doi:10.2307/2531910> and Cheng and He (2021) (under review).
	"""
	
	homepage = "https://github.com/hcheng99/nphPower"
	cran = "nphPower" 

	version("1.0.0", md5="b765f93ff1a15a84011f5523e8d166c2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
