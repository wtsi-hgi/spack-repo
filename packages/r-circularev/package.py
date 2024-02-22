# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircularev(RPackage):
	"""Extreme Value Analysis for Circular Data

	General functions for performing extreme value analysis on a circular 
    domain as part of the statistical methodology in the paper by Konzen, E., 
    Neves, C., and Jonathan, P. (2021). Modeling nonstationary extremes of storm severity: Comparing parametric and semiparametric inference. Environmetrics, 32(4), e2667.
	"""
	
	cran = "circularEV" 

	version("0.1.1", md5="a614ba6f62075ead0de3e8dbf2ba0d21")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-npcirc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
