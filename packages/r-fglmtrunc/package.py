# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFglmtrunc(RPackage):
	"""Truncated Functional Generalized Linear Models

	An implementation of the methodologies described in Xi Liu, Afshin A. Divani, and Alexander Petersen (2022) <doi:10.1016/j.csda.2022.107421>, including 
                truncated functional linear and truncated functional logistic regression models.
	"""
	
	cran = "FGLMtrunc" 

	version("0.1.0", md5="cad35b807625bd270fbed46c8d95526d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
