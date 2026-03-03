# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobkf(RPackage):
	"""Innovative and/or Additive Outlier Robust Kalman Filtering

	Implements a series of robust Kalman filtering approaches. It implements the additive outlier robust filters of Ruckdeschel et al. (2014) <arXiv:1204.3358> and Agamennoni et al. (2018) <doi:10.1109/ICRA.2011.5979605>, the innovative outlier robust filter of Ruckdeschel et al. (2014) <arXiv:1204.3358>, as well as the innovative and additive outlier robust filter of Fisch et al. (2020) <arXiv:2007.03238>.
	"""
	
	cran = "RobKF" 

	version("1.0.2", md5="43287ff903816e0fb4130132413861bb")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
