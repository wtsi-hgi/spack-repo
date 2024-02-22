# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaliberrfimpute(RPackage):
	"""Multiple Imputation Using MICE and Random Forest

	Functions to impute using random forest under full conditional specifications (multivariate imputation by chained equations). The methods are described in Shah and others (2014) <doi:10.1093/aje/kwt312>.
	"""
	
	cran = "CALIBERrfimpute" 

	version("1.0-7", md5="6555b21b2f32eb531f1bd374f048d2e4")

	depends_on("r-mice@2.20:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
