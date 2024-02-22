# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcapp(RPackage):
	"""(Robust) Canonical Correlation Analysis via Projection Pursuit

	Canonical correlation analysis and maximum correlation via
    projection pursuit, as well as fast implementations of correlation
    estimators, with a focus on robust and nonparametric methods.
	"""
	
	cran = "ccaPP" 

	version("0.3.3", md5="164337357e7bd486ab8745a17f2def97")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-pcapp@1.8.1:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.4.100:", type=("build", "run"))
