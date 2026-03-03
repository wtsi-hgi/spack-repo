# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmc(RPackage):
	"""Fitting Generalized Linear Models Subject to Constraints

	Fits generalized linear models where the parameters are subject to linear constraints. The model is specified by giving a symbolic description of the linear predictor, a description of the error distribution, and a matrix of constraints on the parameters.
	"""
	
	cran = "glmc" 

	version("0.3-1", md5="fee146f28151ba3214ee3f0927a55cd8")

	depends_on("r-emplik", type=("build", "run"))
