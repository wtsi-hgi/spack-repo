# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdsa(RPackage):
	"""Time-Dependent Sensitivity Analysis

	Functions that can be used to calculate time-dependent state and parameter sensitivities for both continuous- and discrete-time deterministic models. See Ng et al. (in press) <doi:10.1086/726143> for more information about time-dependent sensitivity analysis.
	"""
	
	homepage = "https://github.com/weehaong/tdsa"
	cran = "tdsa" 

	version("1.1-0", md5="109d6ac7bdd43c031006e9165b58d676")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-desolve@1.10.6:", type=("build", "run"))
	depends_on("r-mathjaxr@0.8.3:", type=("build", "run"))
	depends_on("r-numderiv@2006.4.1:", type=("build", "run"))
