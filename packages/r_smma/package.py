# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmma(RPackage):
	"""Soft Maximin Estimation for Large Scale Array-Tensor Models

	Efficient design matrix free procedure for solving a soft maximin problem for  large scale array-tensor structured models, see Lund, Mogensen and Hansen (2019) <arXiv:1805.02407>. Currently Lasso and SCAD penalized estimation is implemented.
	"""
	
	cran = "SMMA" 

	version("1.0.3", md5="2a158b06f67832b4434c38dd7fa4e7dc")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
