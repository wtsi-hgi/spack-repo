# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStartdesign(RPackage):
	"""Single to Double Arm Transition Design for Phase II Clinical
Trials

	The package is used for calibrating the design parameters for single-to-double arm transition design proposed by Shi and Yin (2017). The calibration is performed via numerical enumeration to find the optimal design that satisfies the constraints on the type I and II error rates.
	"""
	
	cran = "STARTdesign" 

	version("1.0", md5="9f6431f1fe977a6b4b7a37a0d4a22691")

	depends_on("r-rcpp", type=("build", "run"))
