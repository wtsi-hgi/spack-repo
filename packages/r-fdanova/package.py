# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdanova(RPackage):
	"""Analysis of Variance for Univariate and Multivariate Functional
Data

	Performs analysis of variance testing procedures for univariate and multivariate functional data (Cuesta-Albertos and Febrero-Bande (2010) <doi:10.1007/s11749-010-0185-3>, Gorecki and Smaga (2015) <doi:10.1007/s00180-015-0555-0>, Gorecki and Smaga (2017) <doi:10.1080/02664763.2016.1247791>, Zhang et al. (2018) <doi:10.1016/j.csda.2018.05.004>).
	"""
	
	cran = "fdANOVA" 

	version("0.1.2", md5="3f7810f0ba18e93f9261da3156c39977")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-doby", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
