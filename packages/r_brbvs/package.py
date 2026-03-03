# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrbvs(RPackage):
	"""Variable Ranking in Copula Survival Models Affected by General
Censoring Scheme

	Performs variable ranking based on several measures for the class of copula survival model(s) in high dimensional domain.
    The package is based on the class of copula survival model(s) implemented in the 'GJRM' package.
	"""
	
	cran = "BRBVS" 

	version("0.1.1", md5="97082452da2b4a14d8427ed2d2436603")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-copent@0.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.3:", type=("build", "run"))
	depends_on("r-gjrm@0.2.6.4:", type=("build", "run"))
	depends_on("r-mvtnorm@1.2.4:", type=("build", "run"))
