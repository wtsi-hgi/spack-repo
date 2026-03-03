# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalpaf(RPackage):
	"""Causal Effect for Population Attributable Fractions (PAF)

	Calculates population attributable fraction causal effects.
    The 'causalPAF' package contains a suite of functions for causal
    analysis calculations of population attributable fractions (PAF) given
    a causal diagram which apply both: Pathway-specific population
    attributable fractions (PS-PAFs) O’Connell and Ferguson (2022)
    <doi:10.1093/ije/dyac079> and Sequential population attributable
    fractions Ferguson, O’Connell, and O’Donnell (2020)
    <doi:10.1186/s13690-020-00442-x>.  Results are presentable in both
    table and plot format.
	"""
	
	homepage = "https://github.com/MauriceOConnell/causalPAF"
	cran = "causalPAF" 

	version("1.2.5", md5="387f5097106177599cd7094f908bcba7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dagitty", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-ggdag", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
