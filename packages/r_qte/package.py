# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQte(RPackage):
	"""Quantile Treatment Effects

	Provides several methods for computing the Quantile Treatment Effect (QTE) and Quantile Treatment Effect on the Treated (QTT). The main cases covered are (i) Treatment is randomly assigned, (ii) Treatment is as good as randomly assigned after conditioning on some covariates (also called conditional independence or selection on observables) using the methods developed in Firpo (2007) <doi:10.1111/j.1468-0262.2007.00738.x>, (iii) Identification is based on a Difference in Differences assumption (several varieties are available in the package e.g. Athey and Imbens (2006) <doi:10.1111/j.1468-0262.2006.00668.x> Callaway and Li (2019) <doi:10.3982/QE935>, Callaway, Li, and Oka (2018) <doi:10.1016/j.jeconom.2018.06.008>).
	"""
	
	cran = "qte" 

	version("1.3.1", md5="6ddf297c24595d81aef82d1ecc02b046")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-bmisc", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-texreg", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
