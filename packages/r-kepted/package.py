# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKepted(RPackage):
	"""Kernel-Embedding-of-Probability Test for Elliptical Distribution

	Provides an implementation of a kernel-embedding of probability test for elliptical distribution. This is an asymptotic test for elliptical distribution under general alternatives, and the location and shape parameters are assumed to be unknown. Some side-products are posted, including the transformation between rectangular and polar coordinates and two product-type kernel functions. See Tang and Li (2024) <arXiv:2306.10594> for details.
	"""
	
	homepage = "https://github.com/tyy20/KEPTED"
	cran = "KEPTED" 

	version("0.1.0", md5="3c182bcaf4b8464444d3672c90fcfaa5")

	depends_on("r-expm", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
