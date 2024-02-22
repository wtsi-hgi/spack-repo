# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScglr(RPackage):
	"""Supervised Component Generalized Linear Regression

	
    An extension of the Fisher Scoring Algorithm to combine PLS regression with GLM 
    estimation in the multivariate context. Covariates can also be grouped in themes.
	"""
	
	homepage = "https://scnext.github.io/SCGLR"
	cran = "SCGLR" 

	version("3.0", md5="b054a4728f5a12696e6df84d96a6ee9f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
