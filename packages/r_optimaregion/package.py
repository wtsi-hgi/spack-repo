# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimaregion(RPackage):
	"""Confidence Regions for Optima of Response Surfaces

	Computes confidence regions on the location of response surface optima. Response surface models can be up to cubic polynomial models in up to 5 controllable factors, or Thin Plate Spline models in 2 controllable factors.
	"""
	
	cran = "OptimaRegion" 

	version("1.2", md5="0a3e0aa9e7f530c399562a002757ac4a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-depthproc", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rsm", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rdsdp", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
