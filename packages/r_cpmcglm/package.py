# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpmcglm(RPackage):
	"""Correction of the P-Value after Multiple Coding in Generalized
Linear Models

	We propose to determine the correction of the significance level after multiple coding of an explanatory variable in Generalized Linear Model. The different methods of correction of the p-value are the Single step Bonferroni procedure, and resampling based methods developed by P.H.Westfall in 1993. Resampling methods are based on the permutation and the parametric bootstrap procedure. If some continuous, and dichotomous transformations are performed this package offers an exact correction of the p-value developed by B.Liquet & D.Commenges in 2005. The naive method with no correction is also available.
	"""
	
	homepage = "https://cran.r-project.org/"
	cran = "CPMCGLM" 

	version("1.2", md5="efd23aab0659bb3224272f099467ae71")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
