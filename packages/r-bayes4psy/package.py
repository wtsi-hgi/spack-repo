# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayes4psy(RPackage):
	"""User Friendly Bayesian Data Analysis for Psychology

	Contains several Bayesian models for data analysis of psychological tests. A user friendly interface for these models should enable students and researchers to perform professional level Bayesian data analysis without advanced knowledge in programming and Bayesian statistics. This package is based on the Stan platform (Carpenter et el. 2017 <doi:10.18637/jss.v076.i01>).
	"""
	
	homepage = "https://github.com/bstatcomp/bayes4psy"
	cran = "bayes4psy" 

	version("1.2.12", md5="84955f4df11ffee2e6b17d8797f80328")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp@1.0.5:", type=("build", "run"))
	depends_on("r-circular@0.4.93:", type=("build", "run"))
	depends_on("r-cowplot@1.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-emg@1.0.9:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-metrology@0.9.28.1:", type=("build", "run"))
	depends_on("r-reshape@0.8.8:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-mcmcse@1.4.1:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-bh@1.72.0.3:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.7:", type=("build", "run"))
