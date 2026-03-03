# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinalsize(RPackage):
	"""Calculate the Final Size of an Epidemic

	Calculate the final size of a susceptible-infectious-recovered epidemic in a population with demographic variation in contact patterns and susceptibility to disease, as discussed in Miller (2012) <doi:10.1007/s11538-012-9749-6>.
	"""
	
	homepage = "https://github.com/epiverse-trace/finalsize"
	cran = "finalsize" 

	version("0.2.0", md5="e03662e00b0029e6c8e4e732d23e25ca")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
