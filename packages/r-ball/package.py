# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBall(RPackage):
	"""Statistical Inference and Sure Independence Screening via Ball
Statistics

	Hypothesis tests and sure independence screening (SIS) procedure based on ball statistics, including ball divergence <doi:10.1214/17-AOS1579>, ball covariance <doi:10.1080/01621459.2018.1543600>, and ball correlation <doi:10.1080/01621459.2018.1462709>, are developed to analyze complex data in metric spaces, e.g, shape, directional, compositional and symmetric positive definite matrix data. The ball divergence and ball covariance based distribution-free tests are implemented to detecting distribution difference and association in metric spaces <doi:10.18637/jss.v097.i06>. Furthermore, several generic non-parametric feature selection procedures based on ball correlation, BCor-SIS and all of its variants, are implemented to tackle the challenge in the context of ultra high dimensional data. A fast implementation for large-scale multiple K-sample testing with ball divergence <doi: 10.1002/gepi.22423> is supported, which is particularly helpful for genome-wide association study.
	"""
	
	homepage = "https://mamba413.github.io/Ball/"
	cran = "Ball" 

	version("1.3.13", md5="57a28c4a7d3288c179aa3d72ee55ad97")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
