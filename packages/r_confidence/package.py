# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfidence(RPackage):
	"""Confidence Estimation of Environmental State Classifications

	Functions for estimating and reporting multi-year averages and
    corresponding confidence intervals and distributions. A potential use case
    is reporting the chemical and ecological status of surface waters according
    to the European Water Framework Directive.
	"""
	
	cran = "confidence" 

	version("1.1-2", md5="c6f8268bdca48681f12ddc5ea2e7e68c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
