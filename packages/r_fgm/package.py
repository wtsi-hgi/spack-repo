# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgm(RPackage):
	"""Partial Separability and Functional Gaussian Graphical Models

	Estimates a functional graphical model and a partially separable Karhunen-Loève decomposition for a multivariate Gaussian process. See Zapata J., Oh S. and Petersen A. (2019) <arXiv:1910.03134>.
	"""
	
	cran = "fgm" 

	version("1.0", md5="fced2b971b85332ef089930d81fa670d")

	depends_on("r-jgl", type=("build", "run"))
	depends_on("r-fdapace", type=("build", "run"))
