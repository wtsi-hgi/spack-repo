# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConformalinferenceMulti(RPackage):
	"""Conformal Inference Tools for Regression with Multivariate
Response

	It computes full conformal, split conformal and multi split
    conformal prediction regions when the response variable is
    multivariate (i.e. dimension is greater than one). Moreover, the
    package also contain plot functions to visualize the output of the
    full and split conformal functions. 
    To guarantee consistency, the package structure mimics the univariate 'conformalInference'
    package of professor Ryan Tibshirani.
    The main references for the code are: 
    Lei et al. (2016) <arXiv:1604.04173>,
    Diquigiovanni, Fontana, and Vantini (2021) <arXiv:2102.06746>, 
    Diquigiovanni, Fontana, and Vantini (2021) <arXiv:2106.01792>,
    Solari, and Djordjilovic (2021) <arXiv:2103.00627>.
	"""
	
	homepage = "https://github.com/ryantibs/conformal"
	cran = "conformalInference.multi" 

	version("1.1.1", md5="33b21ee31da8385dd97b33fc61143fb3")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-future@1.23:", type=("build", "run"))
	depends_on("r-future-apply@1.8.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-hrbrthemes", type=("build", "run"))
