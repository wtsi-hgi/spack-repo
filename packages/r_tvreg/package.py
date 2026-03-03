# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTvreg(RPackage):
	"""Time-Varying Coefficient for Single and Multi-Equation
Regressions

	Fitting time-varying coefficient models for single and multi-equation regressions, using kernel smoothing techniques.
	"""
	
	homepage = "https://github.com/icasas/tvReg"
	cran = "tvReg" 

	version("0.5.9", md5="bd0a924244b70082ab8ac377c678861f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-systemfit@1.1.20:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-bvarsv", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
