# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarEtp(RPackage):
	"""VAR Modelling: Estimation, Testing, and Prediction

	A collection of the functions for estimation, hypothesis testing, prediction for stationary vector autoregressive models.
	"""
	
	cran = "VAR.etp" 

	version("1.1", md5="f1e9385290af49dd544aebe6f13e679a")

