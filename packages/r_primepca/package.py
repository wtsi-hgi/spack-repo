# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrimepca(RPackage):
	"""Projected Refinement for Imputation of Missing Entries in PCA

	Implements the primePCA algorithm, developed and analysed in Zhu, Z., Wang, T. and Samworth, R. J. (2019) High-dimensional principal component analysis with heterogeneous missingness. <arXiv:1906.12125>.
	"""
	
	cran = "primePCA" 

	version("1.2", md5="1095fb227df2cf7505229f597c6b4726")

	depends_on("r-softimpute", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
