# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsbs(RPackage):
	"""Bandwidth Selection for Level Sets and HDR Estimation

	Bandwidth selection for kernel density estimators of 2-d
    level sets and highest density regions. It applies a plug-in
    strategy to estimate the asymptotic risk function and minimize to
    get the optimal bandwidth matrix. See Doss and Weng (2018)
    <arXiv:1806.00731> for more detail.
	"""
	
	homepage = "http://arxiv.org/abs/1806.00731"
	cran = "lsbs" 

	version("0.1", md5="99654e6645e44e500bcff142a63d5ff3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
