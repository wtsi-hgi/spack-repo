# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelliptical(RPackage):
	"""The Truncated Elliptical Family of Distributions

	It offers random numbers generation from members of the truncated multivariate elliptical family of distribution such as the truncated versions of the Normal, Student-t, Laplace, Pearson VII, Slash, Logistic, among others. Particular distributions can be provided by specifying the density generating function. It also computes the first two moments (covariance matrix as well) for some particular distributions.
  References used for this package: Galarza, C. E., Matos, L. A., Castro, L. M., and Lachos, V. H. (2022). Moments of the doubly truncated selection elliptical distributions with emphasis on the unified multivariate skew-t distribution. Journal of Multivariate Analysis, 189, 104944 <doi:10.1016/j.jmva.2021.104944>; Ho, H. J., Lin, T. I., Chen, H. Y., and Wang, W. L. (2012). Some results on the truncated multivariate t distribution. Journal of Statistical Planning and Inference, 142(1), 25-40 <doi:10.1016/j.jspi.2011.06.006>; Valeriano, K. A., Galarza, C. E., and Matos, L. A. (2021). Moments and random number generation for the truncated elliptical family of distributions. Statistics and Computing, 33(1), 32 <doi:10.1007/s11222-022-10200-4>.
	"""
	
	cran = "relliptical" 

	version("1.3.0", md5="72b2a590216e5d8bca0a0878569b1917")

	depends_on("r-fuzzynumbers-ext-2", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ryacas0", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
