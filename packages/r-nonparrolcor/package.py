# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonparrolcor(RPackage):
	"""a Non-Parametric Statistical Significance Test for Rolling
Window Correlation

	Estimates and plots (as a single plot and as a heat map) the rolling window correlation coefficients between two time series and computes their statistical significance, which is carried out through a non-parametric computing-intensive method. This method addresses the effects due to the multiple testing (inflation of the Type I error) when the statistical significance is estimated for the rolling window correlation coefficients. The method is based on Monte Carlo simulations by permuting one of the variables (e.g., the dependent) under analysis and keeping fixed the other variable (e.g., the independent). We improve the computational efficiency of this method to reduce the computation time through parallel computing. The 'NonParRolCor' package also provides examples with synthetic and real-life environmental time series to exemplify its use. Methods derived from R. Telford (2013) <https://quantpalaeo.wordpress.com/2013/01/04/> and J.M. Polanco-Martinez and J.L. Lopez-Martinez (2021) <doi:10.1016/j.ecoinf.2021.101379>.
	"""
	
	cran = "NonParRolCor" 

	version("0.8.0", md5="de78b9c43af28bc82b617fceda643a54")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
