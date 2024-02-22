# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChangepoints(RPackage):
	"""A Collection of Change-Point Detection Methods

	Performs a series of offline and/or online change-point detection algorithms for 1) univariate mean: <doi:10.1214/20-EJS1710>, <arXiv:2006.03283>; 2) univariate polynomials: <doi:10.1214/21-EJS1963>; 3) univariate and multivariate nonparametric settings: <doi:10.1214/21-EJS1809>, <doi:10.1109/TIT.2021.3130330>; 4) high-dimensional covariances: <doi:10.3150/20-BEJ1249>; 5) high-dimensional networks with and without missing values: <doi:10.1214/20-AOS1953>, <arXiv:2101.05477>, <arXiv:2110.06450>; 6) high-dimensional linear regression models: <arXiv:2010.10410>, <arXiv:2207.12453>; 7) high-dimensional vector autoregressive models: <arXiv:1909.06359>; 8) high-dimensional self exciting point processes: <arXiv:2006.03572>; 9) dependent dynamic nonparametric random dot product graphs: <arXiv:1911.07494>; 10) univariate mean against adversarial attacks: <arXiv:2105.10417>.
	"""
	
	homepage = "https://github.com/HaotianXu/changepoints"
	cran = "changepoints" 

	version("1.1.0", md5="bc5ddb12412d6573f9d2356b901f9b89")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gglasso", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
