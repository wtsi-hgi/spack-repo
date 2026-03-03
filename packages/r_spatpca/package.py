# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatpca(RPackage):
	"""Regularized Principal Component Analysis for Spatial Data

	Provide regularized principal component analysis incorporating smoothness, sparseness and orthogonality of eigen-functions
  by using the alternating direction method of multipliers algorithm (Wang and Huang, 2017, <DOI:10.1080/10618600.2016.1157483>). The
  method can be applied to either regularly or irregularly spaced data, including 1D, 2D, and 3D.
	"""
	
	homepage = "https://github.com/egpivo/SpatPCA"
	cran = "SpatPCA" 

	version("1.3.5", md5="52655f44aae4690d206750c07ca3eb05")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
