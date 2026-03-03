# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPorridge(RPackage):
	"""Ridge-Type Penalized Estimation of a Potpourri of Models

	The name of the package is derived from the French, 'pour' ridge, and provides functionality for ridge-type estimation of a potpourri of models. Currently, this estimation concerns that of various Gaussian graphical models from different study designs. Among others it considers the regular Gaussian graphical model and a mixture of such models. The porridge-package implements the estimation of the former either from i) data with replicated observations by penalized loglikelihood maximization using the regular ridge penalty on the parameters (van Wieringen, Chen, 2021) or ii) from non-replicated data by means of either a ridge estimator with multiple shrinkage targets (as presented in van Wieringen et al. 2020, <doi:10.1016/j.jmva.2020.104621>) or the generalized ridge estimator that allows for both the inclusion of quantitative and qualitative prior information on the precision matrix via element-wise penalization and shrinkage (van Wieringen, 2019, <doi:10.1080/10618600.2019.1604374>). Additionally, the porridge-package facilitates the ridge penalized estimation of a mixture of Gaussian graphical models (Aflakparast et al., 2018). On another note, the package also includes functionality for ridge-type estimation of the generalized linear model (as presented in van Wieringen, Binder, 2022, <doi:10.1080/10618600.2022.2035231>). 
	"""
	
	homepage = "https://www.math.vu.nl/~wvanwie/"
	cran = "porridge" 

	version("0.3.3", md5="51fa68c37c8ef3da0fb73b3ef5904073")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
