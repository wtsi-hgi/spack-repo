# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMomentuhmm(RPackage):
	"""Maximum Likelihood Analysis of Animal Movement Behavior Using
Multivariate Hidden Markov Models

	Extended tools for analyzing telemetry data using generalized hidden Markov models. Features of momentuHMM (pronounced ``momentum'') include data pre-processing and visualization, fitting HMMs to location and auxiliary biotelemetry or environmental data, biased and correlated random walk movement models, hierarchical HMMs, multiple imputation for incorporating location measurement error and missing data, user-specified design matrices and constraints for covariate modelling of parameters, random effects, decoding of the state process, visualization of fitted models, model checking and selection, and simulation. See McClintock and Michelot (2018) <doi:10.1111/2041-210X.12995>.
	"""
	
	homepage = "https://github.com/bmcclintock/momentuHMM"
	cran = "momentuHMM" 

	version("1.5.5", md5="443ab0d389da0c29687483750b012bd8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-circstats", type=("build", "run"))
	depends_on("r-crawl@2.2.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-brobdingnag", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
