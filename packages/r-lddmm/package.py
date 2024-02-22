# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLddmm(RPackage):
	"""Longitudinal Drift-Diffusion Mixed Models (LDDMM)

	Implementation of the drift-diffusion mixed model for category learning as described in Paulon et al. (2021) <doi:10.1080/01621459.2020.1801448>.
	"""
	
	cran = "lddmm" 

	version("0.4.2", md5="241cd877223ec28ed6e8710117ef46c4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rgen", type=("build", "run"))
