# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNrejections(RPackage):
	"""Metrics for Multiple Testing with Correlated Outcomes

	Implements methods in Mathur and VanderWeele (in preparation) to characterize global evidence strength across W correlated ordinary least squares (OLS) hypothesis tests. Specifically, uses resampling to estimate a null interval for the total number of rejections in, for example, 95% of samples generated with no associations (the global null), the excess hits (the difference between the observed number of rejections and the upper limit of the null interval), and a test of the global null based on the number of rejections.
	"""
	
	cran = "NRejections" 

	version("1.2.0", md5="bb749040fc57996dec5a5edd89b22c82")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-stepwisetest", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
