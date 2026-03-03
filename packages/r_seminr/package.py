# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeminr(RPackage):
	"""Building and Estimating Structural Equation Models

	A powerful, easy to syntax for specifying and estimating complex 
    Structural Equation Models. Models can be estimated using Partial 
    Least Squares Path Modeling or Covariance-Based Structural Equation 
    Modeling or covariance based Confirmatory Factor Analysis. Methods described in Ray, Danks, and Valdez (2021).
	"""
	
	cran = "seminr" 

	version("2.3.2", md5="e08a4da01cf6c9e7d85f4fde1c15ea4a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-diagrammer@1.0.6:", type=("build", "run"))
	depends_on("r-diagrammersvg@0.1:", type=("build", "run"))
	depends_on("r-webp", type=("build", "run"))
