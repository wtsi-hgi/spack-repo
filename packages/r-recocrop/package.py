# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecocrop(RPackage):
	"""Estimating Environmental Suitability for Plants

	The ecocrop model estimates environmental suitability for plants using a limiting factor approach for plant growth following Hackett (1991) <doi:10.1007/BF00045728>. The implementation in this package is fast and flexible: it allows for the use of any (environmental) predictor variable. Predictors can be either static (for example, soil pH) or dynamic (for example, monthly precipitation).
	"""
	
	homepage = "https://github.com/cropmodels/Recocrop/"
	cran = "Recocrop" 

	version("0.4-1", md5="6e8678d6cba45b4341754168547012ba")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-meteor", type=("build", "run"))
	depends_on("r-terra@1.1.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
