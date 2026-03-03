# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDgpsi(RPackage):
	"""Interface to 'dgpsi' for Deep and Linked Gaussian Process
Emulations

	Interface to the 'python' package 'dgpsi' for Gaussian process, deep Gaussian process, 
             and linked deep Gaussian process emulations of computer models and networks using stochastic imputation (SI). 
             The implementations follow Ming & Guillas (2021) <doi:10.1137/20M1323771> and 
             Ming, Williamson, & Guillas (2023) <doi:10.1080/00401706.2022.2124311> and 
             Ming & Williamson (2023) <arXiv:2306.01212>. To get started with the package, 
             see <https://mingdeyu.github.io/dgpsi-R/>.
	"""
	
	homepage = "https://github.com/mingdeyu/dgpsi-R"
	cran = "dgpsi" 

	version("2.4.0", md5="c016186620e97ebc964584dd1a2d95f4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-reticulate@1.26:", type=("build", "run"))
	depends_on("r-benchmarkme@1.0.8:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-clhs", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
