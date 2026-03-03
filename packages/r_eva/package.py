# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REva(RPackage):
	"""Extreme Value Analysis with Goodness-of-Fit Testing

	Goodness-of-fit tests for selection of r in the r-largest order
    statistics (GEVr) model. Goodness-of-fit tests for threshold selection in the
    Generalized Pareto distribution (GPD). Random number generation and density functions
    for the GEVr distribution. Profile likelihood for return level estimation
    using the GEVr and Generalized Pareto distributions. P-value adjustments for
    sequential, multiple testing error control. Non-stationary fitting of GEVr and
    GPD.
    Bader, B., Yan, J. & Zhang, X. (2016) <doi:10.1007/s11222-016-9697-3>.
    Bader, B., Yan, J. & Zhang, X. (2018) <doi:10.1214/17-AOAS1092>.
	"""
	
	homepage = "https://github.com/brianbader/eva_package"
	cran = "eva" 

	version("0.2.6", md5="abf4cde5b6cac09d23f17178de70491e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
