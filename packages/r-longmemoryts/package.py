# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongmemoryts(RPackage):
	"""Long Memory Time Series

	Long Memory Time Series is a collection of functions for estimation, simulation and testing of long memory processes, spurious long memory processes and fractionally cointegrated systems. 
	"""
	
	cran = "LongMemoryTS" 

	version("0.1.0", md5="104f6eb7860c13310e2f4203a7bb1d63")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-longmemo", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
