# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecisionsupport(RPackage):
	"""Quantitative Support of Decision Making under Uncertainty

	Supporting the quantitative analysis of binary welfare based
    decision making processes using Monte Carlo simulations. Decision support
    is given on two levels: (i) The actual decision level is to choose between
    two alternatives under probabilistic uncertainty. This package calculates
    the optimal decision based on maximizing expected welfare. (ii) The meta
    decision level is to allocate resources to reduce the uncertainty in the
    underlying decision problem, i.e to increase the current information to
    improve the actual decision making process. This problem is dealt with
    using the Value of Information Analysis. The Expected Value of
    Information for arbitrary prospective estimates can be calculated as
    well as Individual Expected Value of Perfect Information.
    The probabilistic calculations are done via Monte Carlo
    simulations. This Monte Carlo functionality can be used on its own.
	"""
	
	homepage = "http://www.worldagroforestry.org/"
	cran = "decisionSupport" 

	version("1.113", md5="43ab8698bf76cdabd97394bdc5f0420a")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-chillr@0.62:", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fancova@0.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-ggstance", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-msm@1.5:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.2:", type=("build", "run"))
	depends_on("r-nleqslv@2.6:", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rriskdistributions@2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
