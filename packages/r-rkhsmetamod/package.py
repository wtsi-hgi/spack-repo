# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkhsmetamod(RPackage):
	"""Ridge Group Sparse Optimization Problem for Estimation of a Meta
Model Based on Reproducing Kernel Hilbert Spaces

	Estimates the Hoeffding decomposition of an unknown function by solving ridge group sparse optimization problem based on reproducing kernel Hilbert spaces, and approximates its sensitivity indices (see Kamari, H., Huet, S. and Taupin, M.-L. (2019) <arXiv:1905.13695>).
	"""
	
	cran = "RKHSMetaMod" 

	version("1.1", md5="0c2bca0d2ceff71c6a10da7fb518f5fe")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
