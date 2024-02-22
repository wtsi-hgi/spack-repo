# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopksignal(RPackage):
	"""A Convex Optimization Tool for Signal Reconstruction from
Multiple Ranked Lists

	A mathematical optimization procedure in combination with statistical bootstrap for the estimation of the latent signals (sometimes called scores) informing the global consensus ranking (often named aggregation ranking). To solve mid/large-scale problems, users should install the 'gurobi' optimiser (available from <https://www.gurobi.com/>).
	"""
	
	cran = "TopKSignal" 

	version("1.0", md5="8504b909cbead3627f7e2512adbd5f98")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
