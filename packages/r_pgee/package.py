# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgee(RPackage):
	"""Penalized Generalized Estimating Equations in High-Dimension

	Fits penalized generalized estimating equations to longitudinal data with high-dimensional covariates.
	"""
	
	cran = "PGEE" 

	version("1.5", md5="3c009c3725de04c9c1d0a02f9a1b6e16")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
