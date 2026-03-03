# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgmm(RPackage):
	"""Robust Mixture Model

	Algorithms for estimating robustly the parameters of a Gaussian, Student, or Laplace Mixture Model.
	"""
	
	cran = "RGMM" 

	version("2.1.0", md5="8a88268818dcc84877ebfb58d5e7ac78")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-genieclust", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
