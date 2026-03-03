# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLookout(RPackage):
	"""Leave One Out Kernel Density Estimates for Outlier Detection

	Outlier detection using leave-one-out kernel density estimates and
    extreme value theory. The bandwidth for kernel density estimates is computed 
    using persistent homology, a technique in topological data analysis. Using 
    peak-over-threshold method, a generalized Pareto distribution is fitted to
    the log of leave-one-out kde values to identify outliers. 
	"""
	
	homepage = "https://sevvandi.github.io/lookout/"
	cran = "lookout" 

	version("0.1.4", md5="ab34548efa21dae443620ef7f3eca430")

	depends_on("r-tdastats", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
