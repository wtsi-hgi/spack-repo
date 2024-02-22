# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPamm(RPackage):
	"""Power Analysis for Random Effects in Mixed Models

	Simulation functions to assess or explore the power of a dataset to estimates significant random effects (intercept or slope) in a mixed model. The functions are based on the "lme4" and "lmerTest" packages.
	"""
	
	homepage = "https://github.com/JulienGAMartin/pamm_R"
	cran = "pamm" 

	version("1.122", md5="3a9cc951f79c8f8110aa3cb28c02b6f0")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
