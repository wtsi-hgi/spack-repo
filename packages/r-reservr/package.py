# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReservr(RPackage):
	"""Fit Distributions and Neural Networks to Censored and Truncated
Data

	Define distribution families and fit them to
    interval-censored and interval-truncated data, where the truncation
    bounds may depend on the individual observation. The defined
    distributions feature density, probability, sampling and fitting
    methods as well as efficient implementations of the log-density log
    f(x) and log-probability log P(x0 <= X <= x1) for use in 'TensorFlow'
    neural networks via the 'tensorflow' package. Allows training
    parametric neural networks on interval-censored and interval-truncated
    data with flexible parameterization. Applications include Claims
    Development in Non-Life Insurance, e.g. modelling reporting delay
    distributions from incomplete data, see Bücher, Rosenstock (2022)
    <doi:10.1007/s13385-022-00314-4>.
	"""
	
	homepage = "https://ashesitr.github.io/reservr/"
	cran = "reservr" 

	version("0.0.2", md5="e091734d1e3a9ec4d172edf35ad9d842")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-keras@2.2.5:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
