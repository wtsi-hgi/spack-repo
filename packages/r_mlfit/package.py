# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlfit(RPackage):
	"""Iterative Proportional Fitting Algorithms for Nested Structures

	The Iterative Proportional Fitting (IPF) algorithm operates on count data. 
    This package offers implementations for several algorithms that extend this to 
    nested structures: 'parent' and 'child' items for both of which constraints can be provided.
    The fitting algorithms include Iterative Proportional Updating <https://trid.trb.org/view/881554>,
    Hierarchical IPF <doi:10.3929/ethz-a-006620748>, Entropy Optimization <https://trid.trb.org/view/881144>,
    and Generalized Raking <doi:10.2307/2290793>. Additionally, a number of replication methods
    is also provided such as 'Truncate, replicate, sample' <doi:10.1016/j.compenvurbsys.2013.03.004>. 
	"""
	
	homepage = "https://mlfit.github.io/mlfit/"
	cran = "mlfit" 

	version("0.5.3", md5="e043caa7a95020024fe68dbd64336e79")

	depends_on("r-bb", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-kimisc", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-wrswor", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
