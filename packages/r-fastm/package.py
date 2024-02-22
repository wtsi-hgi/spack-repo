# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastm(RPackage):
	"""Fast Computation of Multivariate M-Estimators

	Implements the new algorithm for fast computation of M-scatter matrices using a partial Newton-Raphson procedure for several estimators. The algorithm is described in Duembgen, Nordhausen and Schuhmacher (2016) <doi:10.1016/j.jmva.2015.11.009>. 
	"""
	
	cran = "fastM" 

	version("0.0-4", md5="97103bfd75ed34de9cd6e9b384a32b59")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
