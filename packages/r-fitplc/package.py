# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitplc(RPackage):
	"""Fit Hydraulic Vulnerability Curves

	Fits Weibull or sigmoidal models to percent loss conductivity (plc) curves as a function of plant water potential, computes confidence intervals of parameter estimates and predictions with bootstrap or parametric methods, and provides convenient plotting methods.
	"""
	
	homepage = "https://www.bitbucket.org/remkoduursma/fitplc"
	cran = "fitplc" 

	version("1.2-3", md5="c230b2faeb6a07c8ce549e1ec48d5e8e")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
