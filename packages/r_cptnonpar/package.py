# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCptnonpar(RPackage):
	"""Nonparametric Change Point Detection for Multivariate Time
Series

	Implements the nonparametric moving sum procedure for detecting 
    changes in the joint characteristic function (NP-MOJO) for multiple change
    point detection in multivariate time series. See McGonigle, E. T., Cho, H. 
    (2023) <arXiv:2305.07581> for description of the NP-MOJO methodology.
	"""
	
	homepage = "https://github.com/EuanMcGonigle/CptNonPar"
	cran = "CptNonPar" 

	version("0.1.1", md5="752d80f1d0b409550a68d229400de228")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
