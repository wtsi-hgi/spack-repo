# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFarmtest(RPackage):
	"""Factor-Adjusted Robust Multiple Testing

	Performs robust multiple testing for means in the presence of known and unknown latent factors presented in Fan et al.(2019) "FarmTest: Factor-Adjusted Robust Multiple Testing With Approximate False Discovery Control" <doi:10.1080/01621459.2018.1527700>.
             Implements a series of adaptive Huber methods combined with fast data-drive tuning schemes proposed in Ke et al.(2019) "User-Friendly Covariance Estimation for Heavy-Tailed Distributions" <doi:10.1214/19-STS711> to estimate model parameters and construct test statistics that are robust against heavy-tailed and/or asymmetric error distributions. 
             Extensions to two-sample simultaneous mean comparison problems are also included. 
             As by-products, this package contains functions that compute adaptive Huber mean, covariance and regression estimators that are of independent interest.
	"""
	
	homepage = "https://github.com/XiaoouPan/FarmTest"
	cran = "FarmTest" 

	version("2.2.0", md5="185cc01d120ad795d337aeca1dab4569")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
