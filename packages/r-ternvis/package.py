# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTernvis(RPackage):
	"""Visualisation, Verification and Calibration of Ternary
Probabilistic Forecasts

	A suite of functions for visualising ternary probabilistic forecasts, as discussed in the paper by Jupp (2012) <doi:10.1098/rsta.2011.0350>.
	"""
	
	cran = "ternvis" 

	version("1.2", md5="abe9618c0c3e9b0e9e1df41f97d27915")

	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-dichromat", type=("build", "run"))
