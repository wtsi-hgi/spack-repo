# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDglmextpois(RPackage):
	"""Double Generalized Linear Models Extending Poisson Regression

	Model estimation, dispersion testing and diagnosis of hyper-Poisson
    Saez-Castillo, A.J. and Conde-Sanchez, A. (2013) 
    <doi:10.1016/j.csda.2012.12.009> and Conway-Maxwell-Poisson Huang, A. (2017)
    regression models.
	"""
	
	homepage = "https://github.com/franciscomartinezdelrio/DGLMExtPois"
	cran = "DGLMExtPois" 

	version("0.2.3", md5="4ad719d906d17d81e4ab97c46aa1ddb9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nloptr@1.2.1:", type=("build", "run"))
	depends_on("r-compoissonreg", type=("build", "run"))
