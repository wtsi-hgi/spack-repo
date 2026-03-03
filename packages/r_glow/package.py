# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlow(RPackage):
	"""Make Plots that Glow

	Provides a framework for creating plots with glowing points.
	"""
	
	homepage = "https://github.com/traversc/glow"
	cran = "glow" 

	version("0.11.0", md5="bd71e440111fbfd3ac59e97a6e255d3c")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
