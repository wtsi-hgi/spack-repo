# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbitspatial(RPackage):
	"""Probit with Spatial Dependence, SAR, SEM and SARAR Models

	Fast estimation of binomial spatial probit regression models with spatial autocorrelation for big datasets.
	"""
	
	cran = "ProbitSpatial" 

	version("1.1", md5="ed492fbf1d3337e6682ce76a43085025")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
