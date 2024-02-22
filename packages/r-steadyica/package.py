# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSteadyica(RPackage):
	"""ICA and Tests of Independence via Multivariate Distance
Covariance

	Functions related to multivariate measures of independence and ICA:
 -estimate independent components by minimizing distance covariance;
 -conduct a test of mutual independence based on distance covariance; 
 -estimate independent components via infomax (a popular method but generally performs poorer than mdcovica, ProDenICA, and/or fastICA, but is useful for comparisons);
 -order indepedent components by skewness;
 -match independent components from multiple estimates;
 -other functions useful in ICA.
	"""
	
	cran = "steadyICA" 

	version("1.0", md5="e863936c0b313e46ecf3885d5ba2eecf")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
