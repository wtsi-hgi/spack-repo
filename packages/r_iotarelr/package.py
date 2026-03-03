# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIotarelr(RPackage):
	"""Iota Inter Coder Reliability for Content Analysis

	Routines and tools for assessing the quality of content
    analysis on the basis of the Iota Reliability Concept. The concept is
    inspired by item response theory and can be applied to any kind of
    content analysis which uses a standardized coding scheme and discrete
    categories.  It is also applicable for content analysis conducted by
    artificial intelligence.  The package provides reliability measures
    for a complete scale as well as for every single category. Analysis of
    subgroup-invariance and error corrections are implemented. This
    information can support the development process of a coding scheme and
    allows a detailed inspection of the quality of the generated data.
    Equations and formulas working in this package are part of Berding et
    al. (2022)<doi:10.3389/feduc.2022.818365> and Berding and Pargmann
    (2022) <doi:10.30819/5581>.
	"""
	
	homepage = "https://fberding.github.io/iotarelr/"
	cran = "iotarelr" 

	version("0.1.5", md5="5d7a83c8b701dd53ae088ff2b457fb6d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggalluvial", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
