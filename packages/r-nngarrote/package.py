# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNngarrote(RPackage):
	"""Non-Negative Garrote Estimation with Penalized Initial
Estimators

	Functions to compute the non-negative garrote estimator as 
             proposed by Breiman (1995) <https://www.jstor.org/stable/1269730>
             with the penalized initial estimators extension as proposed by 
             Yuan and Lin (2007) <https://www.jstor.org/stable/4623260>.
	"""
	
	cran = "nnGarrote" 

	version("1.0.4", md5="9e214f487d06bf67c0cc525639de0d0d")

	depends_on("r-glmnet", type=("build", "run"))
