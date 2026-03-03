# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClme(RPackage):
	"""Constrained Inference for Linear Mixed Effects Models

	Estimation and inference for linear models where some or all of the
    fixed-effects coefficients are subject to order restrictions. This package uses
    the robust residual bootstrap methodology for inference, and can handle some
    structure in the residual variance matrix.
	"""
	
	cran = "CLME" 

	version("2.0-12", md5="c715f30fc50cc89eb9402ae94b662d8a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-isotone", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-prettyr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
