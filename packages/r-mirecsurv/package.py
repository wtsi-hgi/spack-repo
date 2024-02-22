# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirecsurv(RPackage):
	"""Left-Censored Recurrent Events Survival Models

	Fitting recurrent events survival models for
    left-censored data with multiple imputation of the number of previous episodes.
    See Hernández-Herrera G, Moriña D, Navarro A. (2020) <arXiv:2007.15031>.
	"""
	
	cran = "miRecSurv" 

	version("1.0.2", md5="f2adc7265630c615c2e0dc9b3554dbd1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-compoissonreg", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
