# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFic(RPackage):
	"""Focused Information Criteria for Model Comparison

	Compares how well different models estimate a quantity of interest (the "focus") so that different models may be preferred for different purposes.  Comparisons within any class of models fitted by maximum likelihood are supported, with shortcuts for commonly-used classes such as generalised linear models and parametric survival models.  The methods originate from Claeskens and Hjort (2003) <doi:10.1198/016214503000000819> and Claeskens and Hjort (2008, ISBN:9780521852258).
	"""
	
	homepage = "https://github.com/chjackson/fic"
	cran = "fic" 

	version("1.0.0", md5="d70ec9b416212abe935a279aeb365452")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
