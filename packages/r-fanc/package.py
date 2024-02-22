# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFanc(RPackage):
	"""Penalized Likelihood Factor Analysis via Nonconvex Penalty

	Computes the penalized maximum likelihood estimates of factor loadings and unique variances for various tuning parameters. The pathwise coordinate descent along with EM algorithm is used.  This package also includes a new graphical tool which outputs path diagram, goodness-of-fit indices and model selection criteria for each regularization parameter. The user can change the regularization parameter by manipulating scrollbars, which is helpful to find a suitable value of regularization parameter.
	"""
	
	homepage = "https://doi.org/10.1007/s11222-014-9458-0"
	cran = "fanc" 

	version("2.3.11", md5="eacad0e624d0097c8687489ba79bd24f")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
