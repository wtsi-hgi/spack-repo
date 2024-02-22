# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoptimus(RPackage):
	"""A Parallel General-Purpose Adaptive Optimisation Engine

	A general-purpose optimisation engine that supports 
	i) Monte Carlo optimisation with Metropolis criterion [Metropolis et al. (1953) <doi:10.1063/1.1699114>, Hastings (1970) <doi:10.1093/biomet/57.1.97>]
    and Acceptance Ratio Simulated Annealing [Kirkpatrick et al. (1983) <doi:10.1126/science.220.4598.671>, Černý (1985) <doi:10.1007/BF00940812>] 
	on multiple cores, and ii) Acceptance Ratio Replica Exchange Monte 
	Carlo Optimisation. In each case, the system pseudo-temperature is 
	dynamically adjusted such that the observed acceptance ratio is kept 
	near to the desired (fixed or changing) acceptance ratio.
	"""
	
	homepage = "https://github.com/SahakyanLab/ROptimus"
	cran = "ROptimus" 

	version("3.0.0", md5="21778a2af00ed064876b7830329acd0d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-doparallel@1.0.11:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-iterators@1.0.9:", type=("build", "run"))
