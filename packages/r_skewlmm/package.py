# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkewlmm(RPackage):
	"""Scale Mixture of Skew-Normal Linear Mixed Models

	It fits scale mixture of skew-normal linear mixed models using an expectation–maximization (EM) type algorithm, including some possibilities for modeling the within-subject dependence. Details can be found in Schumacher, Lachos and Matos (2021) <doi:10.1002/sim.8870>.
	"""
	
	homepage = "https://github.com/fernandalschumacher/skewlmm"
	cran = "skewlmm" 

	version("1.1.0", md5="c8226fe39e7744db32ccc1a44b76252a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-momtrunc", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-relliptical", type=("build", "run"))
	depends_on("r-truncatednormal", type=("build", "run"))
