# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphicalvar(RPackage):
	"""Graphical VAR for Experience Sampling Data

	Estimates within and between time point interactions in experience sampling data, using the Graphical vector autoregression model in combination with regularization. See also Epskamp, Waldorp, Mottus & Borsboom (2018) <doi:10.1080/00273171.2018.1454823>.
	"""
	
	cran = "graphicalVAR" 

	version("0.3.4", md5="e40831eb0978a8faf0bf29eeb5dfb37e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-qgraph@1.3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
