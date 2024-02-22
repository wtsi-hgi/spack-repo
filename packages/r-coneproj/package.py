# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConeproj(RPackage):
	"""Primal or Dual Cone Projections with Routines for Constrained
Regression

	Routines doing cone projection and quadratic programming, as well as doing estimation and inference for constrained parametric regression and shape-restricted regression problems. See Mary C. Meyer (2013)<doi:10.1080/03610918.2012.659820> for more details.
	"""
	
	cran = "coneproj" 

	version("1.17", md5="7921bf1a47aea7bbd5f724ac3062c00e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
