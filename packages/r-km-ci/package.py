# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKmCi(RPackage):
	"""Confidence Intervals for the Kaplan-Meier Estimator

	Computes various confidence intervals for the Kaplan-Meier
        estimator, namely: Peto's CI, Rothman CI, CI's based on
        Greenwood's variance, Thomas and Grunkemeier CI and the
        simultaneous confidence bands by Nair and Hall and Wellner.
	"""
	
	cran = "km.ci" 

	version("0.5-6", md5="557066a7ceeca9074229b12c111c0e27")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
