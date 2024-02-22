# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovtools(RPackage):
	"""Statistical Tools for Covariance Analysis

	Covariance is of universal prevalence across various disciplines within statistics.
    We provide a rich collection of geometric and inferential tools for convenient analysis of
    covariance structures, topics including distance measures, mean covariance estimator,
    covariance hypothesis test for one-sample and two-sample cases, and covariance estimation.
    For an introduction to covariance in multivariate statistical analysis,
    see Schervish (1987) <doi:10.1214/ss/1177013111>.
	"""
	
	homepage = "https://github.com/kisungyou/CovTools"
	cran = "CovTools" 

	version("0.5.4", md5="db470bd83ce1ee0b9d7b3e29f7998847")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-geigen", type=("build", "run"))
	depends_on("r-shapes", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-sht", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
