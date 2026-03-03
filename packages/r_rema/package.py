# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRema(RPackage):
	"""Rare Event Meta Analysis

	The rema package implements a permutation-based approach for binary 
	meta-analyses of 2x2 tables, founded on conditional logistic regression, 
	that provides more reliable statistical tests when heterogeneity is 
	observed in rare event data (Zabriskie et al. 2021 <doi:10.1002/sim.9142>). 
	To adjust for the effect of heterogeneity, this method conditions on the 
	sufficient statistic of a proxy for the heterogeneity effect as opposed to
	estimating the heterogeneity variance. While this results in the model not
	strictly falling under the random-effects framework, it is akin to a 
	random-effects approach in that it assumes differences in variability due 
	to treatment. Further, this method does not rely on large-sample 
	approximations or continuity corrections for rare event data. This method
	uses the permutational distribution of the test statistic instead of
	asymptotic approximations for inference. The number of observed events 
	drives the computation complexity for creating this permutational 
	distribution. Accordingly, for this method to be computationally feasible,
	it should only be applied to meta-analyses with a relatively low number of
	observed events. To create this permutational distribution, a network 
	algorithm, based on the work of Mehta et al. (1992) <doi:10.2307/1390598> 
	and Corcoran et al. (2001) <doi:10.1111/j.0006-341x.2001.00941.x>, is 
	employed using C++ and integrated into the package.
	"""
	
	cran = "rema" 

	version("0.0.1", md5="2583c863b34a25487b6e7089edcf8e24")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
