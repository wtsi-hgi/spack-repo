# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmoments(RPackage):
	"""L-Moments and Quantile Mixtures

	Contains functions to estimate
        L-moments and trimmed L-moments from the data. Also
        contains functions to estimate the parameters of the normal
        polynomial quantile mixture and the Cauchy polynomial quantile
        mixture from L-moments and trimmed L-moments.
	"""
	
	homepage = "http://users.jyu.fi/~jutakarv/"
	cran = "Lmoments" 

	version("1.3-1", md5="9e9704ea64b3a969f09a1f32b7936ccb")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
