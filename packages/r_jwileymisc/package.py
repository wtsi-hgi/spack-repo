# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJwileymisc(RPackage):
	"""Miscellaneous Utilities and Functions

	Miscellaneous tools and functions,
    including: generate descriptive statistics tables,
    format output, visualize relations among variables or check
    distributions, and generic functions for residual and
    model diagnostics. 
	"""
	
	homepage = "https://joshuawiley.com/JWileymisc/"
	cran = "JWileymisc" 

	version("1.4.1", md5="8fda0021f860cf187032dd194fa6b0d6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-ggplot2@3.4.3:", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-lavaan@0.6.16:", type=("build", "run"))
	depends_on("r-vgam@1.1.9:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-extraoperators@0.1.1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
