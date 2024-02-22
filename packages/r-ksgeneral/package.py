# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKsgeneral(RPackage):
	"""Computing P-Values of the K-S Test for (Dis)Continuous Null
Distribution

	Computes a p-value of the one-sample two-sided (or one-sided, as a special case) Kolmogorov-Smirnov (KS) statistic, for any fixed critical level, and an arbitrary, possibly large sample size for a pre-specified purely discrete, mixed or continuous cumulative distribution function (cdf) under the null hypothesis. If a data sample is supplied, 'KSgeneral' computes the p-value corresponding to the value of the KS test statistic computed based on the user provided data sample. The package 'KSgeneral' implements a novel, accurate and efficient method named Exact-KS-FFT, expressing the p-value as a double-boundary non-crossing probability for a homogeneous Poisson process, which is then efficiently computed using Fast Fourier Transform (FFT). The package can also be used to compute and plot the complementary cdf of the KS statistic which is known to depend on the hypothesized distribution when the latter is discontinuous (i.e. purely discrete or mixed). To cite this package in publication use: Dimitrina S. Dimitrova, Vladimir K. Kaishev, and Senren Tan. Computing the Kolmogorov-Smirnov Distribution When the Underlying CDF is Purely Discrete, Mixed, or Continuous. Journal of Statistical Software. 2020; 95(10): 1--42. <doi:10.18637/jss.v095.i10>. 
	"""
	
	homepage = "https://github.com/raymondtsr/KSgeneral"
	cran = "KSgeneral" 

	version("1.1.2", md5="df9966c908fdb020a758216433d627ec")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dgof", type=("build", "run"))
	depends_on("fftw@3.3.4:", type=("build", "link", "run"))
