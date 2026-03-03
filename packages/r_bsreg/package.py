# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsreg(RPackage):
	"""Bayesian Spatial Regression Models

	Fit Bayesian models with a focus on the spatial econometric models.
	"""
	
	cran = "bsreg" 

	version("0.0.2", md5="6a6a824bdd3d112bd65e13ab8711f21b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
