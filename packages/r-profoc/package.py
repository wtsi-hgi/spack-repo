# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfoc(RPackage):
	"""Probabilistic Forecast Combination Using CRPS Learning

	Combine probabilistic forecasts using CRPS learning algorithms proposed in Berrisch, Ziel (2021) <arXiv:2102.00968> <doi:10.1016/j.jeconom.2021.11.008>. The package implements multiple online learning algorithms like Bernstein online aggregation; see Wintenberger (2014) <arXiv:1404.1356>. Quantile regression is also implemented for comparison purposes. Model parameters can be tuned automatically with respect to the loss of the forecast combination. Methods like predict(), update(), plot() and print() are available for convenience. This package utilizes the optim C++ library for numeric optimization <https://github.com/kthohr/optim>.
	"""
	
	homepage = "https://profoc.berrisch.biz"
	cran = "profoc" 

	version("1.3.2", md5="c1290b86e4395de0f1df95ad78f6de7f")
	version("1.3.1", md5="44d5f6241f550d8956f764c234460e1e")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.10.7.5:", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-splines2@0.4.4:", type=("build", "run"))
	depends_on("r-rcpptimer@1.1:", type=("build", "run"))
