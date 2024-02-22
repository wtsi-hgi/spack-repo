# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaeeb(RPackage):
	"""Small Area Estimation for Count Data

	Provides small area estimation for count data type and gives option whether to use covariates in the estimation or not. By implementing Empirical Bayes (EB) Poisson-Gamma model, each function returns EB estimators and mean squared error (MSE) estimators for each area. The EB estimators without covariates are obtained using the model proposed by Clayton & Kaldor (1987) <doi:10.2307/2532003>, the EB estimators with covariates are obtained using the model proposed by Wakefield (2006) <doi:10.1093/biostatistics/kxl008> and the MSE estimators are obtained using Jackknife method by Jiang et. al. (2002) <doi:10.1214/aos/1043351257>.
	"""
	
	cran = "saeeb" 

	version("0.1.0", md5="94f6bff45e85c84b7e0e186c0391cae0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-count@1.3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
