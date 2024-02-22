# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVardetect(RPackage):
	"""Multiple Change Point Detection in Structural VAR Models

	Implementations of Thresholded Block Segmentation Scheme (TBSS) and Low-rank plus Sparse Two Step Procedure (LSTSP) algorithms for detecting multiple changes in structural VAR models. The package aims to address the problem of change point detection in piece-wise stationary VAR models, under different settings regarding the structure of their transition matrices (autoregressive dynamics); specifically, the following cases are included: (i) (weakly) sparse, (ii) structured sparse, and (iii) low rank plus sparse. It includes multiple algorithms and related extensions from Safikhani and Shojaie (2020) <doi:10.1080/01621459.2020.1770097> and Bai, Safikhani and Michailidis (2020) <doi:10.1109/TSP.2020.2993145>.
	"""
	
	cran = "VARDetect" 

	version("0.1.6", md5="7dd5c6748aef10ff10de32774e843796")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mts", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-sparsevar", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
