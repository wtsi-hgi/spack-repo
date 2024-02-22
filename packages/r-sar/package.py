# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSar(RPackage):
	"""Smart Adaptive Recommendations

	'Smart Adaptive Recommendations' (SAR) is the name of a fast, scalable, adaptive algorithm for personalized recommendations based on user transactions and item descriptions. It produces easily explainable/interpretable recommendations and handles "cold item" and "semi-cold user" scenarios. This package provides two implementations of 'SAR': a standalone implementation, and an interface to a web service in Microsoft's 'Azure' cloud: <https://github.com/Microsoft/Product-Recommendations/blob/master/doc/sar.md>. The former allows fast and easy experimentation, and the latter provides robust scalability and extra features for production use.
	"""
	
	homepage = "https://github.com/hongooi73/SAR"
	cran = "SAR" 

	version("1.0.3", md5="a7f63b187467bd94a111e1fe003fffc9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-azurermr", type=("build", "run"))
	depends_on("r-azurestor", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
