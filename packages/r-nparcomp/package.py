# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNparcomp(RPackage):
	"""Multiple Comparisons and Simultaneous Confidence Intervals

	With this package, it is possible to compute nonparametric simultaneous confidence intervals for relative contrast effects in the unbalanced one way layout. Moreover, it computes simultaneous p-values. The simultaneous confidence intervals can be computed using multivariate normal distribution, multivariate t-distribution with a Satterthwaite Approximation of the degree of freedom or using multivariate range preserving transformations with Logit or Probit as transformation function. 2 sample comparisons can be performed with the same methods described above. There is no assumption on the underlying distribution function, only that the data have to be at least ordinal numbers. See Konietschke et al. (2015) <doi:10.18637/jss.v064.i09> for details.
	"""
	
	cran = "nparcomp" 

	version("3.0", md5="bdc9eb65fb4dc3fccc338cef8aa3b1b6")

	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
