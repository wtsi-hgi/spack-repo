# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQfa(RPackage):
	"""Quantile-Frequency Analysis (QFA) of Time Series

	Quantile-frequency analysis (QFA) of univariate or multivariate time series based on trigonometric quantile regression. See Li, T.-H. (2012) "Quantile periodograms", Journal of the American Statistical Association, 107, 765–776, <doi:10.1080/01621459.2012.682815>; Li, T.-H. (2014) Time Series with Mixed Spectra, CRC Press, <doi:10.1201/b15154>; Li, T.-H. (2022) "Quantile Fourier transform, quantile series, and nonparametric estimation of quantile spectra", <doi:10.48550/arXiv.2211.05844>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "qfa" 

	version("2.1", md5="92f1e968c0694225d77385494441f41c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
