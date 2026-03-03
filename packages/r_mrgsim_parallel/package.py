# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrgsimParallel(RPackage):
	"""Simulate with 'mrgsolve' in Parallel

	Simulation from an 'mrgsolve' 
    <https://cran.r-project.org/package=mrgsolve> model using a parallel backend.  
    Input data sets are split (chunked) and simulated in parallel using 
    mclapply() or future_lapply() 
    <https://cran.r-project.org/package=future.apply>.
	"""
	
	homepage = "https://github.com/kylebaron/mrgsim.parallel"
	cran = "mrgsim.parallel" 

	version("0.2.1", md5="4e12e373dafb02b71fc66293b2f4b6e4")

	depends_on("r-mrgsolve", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
