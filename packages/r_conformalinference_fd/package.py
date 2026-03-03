# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConformalinferenceFd(RPackage):
	"""Tools for Conformal Inference for Regression in Multivariate
Functional Setting

	It computes full conformal, split conformal and multi split
    conformal prediction regions when the response has functional nature.
    Moreover, the package also contain a plot function to visualize the
    output of the split conformal.
    To guarantee consistency, the package structure mimics the univariate 
    'conformalInference' package of professor Ryan Tibshirani.
    The main references for the code are: 
    Diquigiovanni, Fontana, and Vantini (2021) <arXiv:2102.06746>, 
    Diquigiovanni, Fontana, and Vantini (2021) <arXiv:2106.01792>,
    Solari, and Djordjilovic (2021) <arXiv:2103.00627>.
	"""
	
	homepage = "https://github.com/ryantibs/conformal"
	cran = "conformalInference.fd" 

	version("1.1.1", md5="f776a9679e81914d4decb9c75db93a1b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-fda@5.5.1:", type=("build", "run"))
	depends_on("r-future@1.23:", type=("build", "run"))
	depends_on("r-future-apply@1.8.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
