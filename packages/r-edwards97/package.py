# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdwards97(RPackage):
	"""Langmuir Semi-Empirical Coagulation Model

	Implements the Edwards (1997) <doi:10.1002/j.1551-8833.1997.tb08229.x>
    Langmuir-based semi-empirical coagulation model, which predicts the concentration
    of organic carbon remaining in water after treatment with an Al- or Fe-based
    coagulant. Data and methods are provided to optimise empirical coefficients.
	"""
	
	homepage = "https://paleolimbot.github.io/edwards97/"
	cran = "edwards97" 

	version("0.1.1", md5="8dedbc2947d6fc7be377ff32ec87c7b1", url="https://cran.r-project.org/src/contrib/edwards97_0.1.1.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
