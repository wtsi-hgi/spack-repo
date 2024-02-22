# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPermuco(RPackage):
	"""Permutation Tests for Regression, (Repeated Measures)
ANOVA/ANCOVA and Comparison of Signals

	Functions to compute p-values based on permutation tests. Regression, ANOVA and ANCOVA, omnibus F-tests, marginal unilateral and bilateral t-tests are available. Several methods to handle nuisance variables are implemented (Kherad-Pajouh, S., & Renaud, O. (2010) <doi:10.1016/j.csda.2010.02.015> ; Kherad-Pajouh, S., & Renaud, O. (2014) <doi:10.1007/s00362-014-0617-3> ; Winkler, A. M., Ridgway, G. R., Webster, M. A., Smith, S. M., & Nichols, T. E. (2014) <doi:10.1016/j.neuroimage.2014.01.060>). An extension for the comparison of signals issued from experimental conditions (e.g. EEG/ERP signals) is provided. Several corrections for multiple testing are possible, including the cluster-mass statistic (Maris, E., & Oostenveld, R. (2007) <doi:10.1016/j.jneumeth.2007.03.024>) and the threshold-free cluster enhancement (Smith, S. M., & Nichols, T. E. (2009) <doi:10.1016/j.neuroimage.2008.03.061>). 
	"""
	
	homepage = "https://github.com/jaromilfrossard/permuco"
	cran = "permuco" 

	version("1.1.2", md5="5b1e146c60cf3f67dedda523721a28ab")

	depends_on("r-permute", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
