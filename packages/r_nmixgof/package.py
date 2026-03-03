# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmixgof(RPackage):
	"""Goodness of Fit Checks for Binomial N-Mixture Models

	Provides residuals and overdispersion metrics to assess the fit of N-mixture models obtained using the package 'unmarked'. 
    Details on the methods are given in Knape et al. (2017) <doi:10.1101/194340>.
	"""
	
	homepage = "https://github.com/jknape/nmixgof"
	cran = "nmixgof" 

	version("0.1.0", md5="cff7ec8afbbb13db11e398b2ecaf1504")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-unmarked", type=("build", "run"))
