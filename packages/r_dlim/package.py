# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlim(RPackage):
	"""Distributed Lag Interaction Model

	Collection of functions for fitting and interpreting distributed lag interaction models (DLIM). A DLIM regresses a scalar outcome on repeated measures of exposure and allows for modification by a continuous variable. Includes a dlim() function for fitting, predict() function for inference, and plotting functions for visualization. Details on methodology are described in Demateis et al. (2024) <doi:10.1002/env.2843>.
	"""
	
	cran = "dlim" 

	version("0.1.0", md5="c06af4d85ac225b0060b3b3278516b9a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dlnm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tsmodel", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
