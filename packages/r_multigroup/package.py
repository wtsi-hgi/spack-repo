# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultigroup(RPackage):
	"""Multigroup Data Analysis

	Multivariate analysis methods including principal component analysis,
    partial least square regression, and multiblock analysis to describe,
    summarize, and visualize data with a group structure.
	"""
	
	cran = "multigroup" 

	version("0.4.5", md5="78f2af54bc4da17965cab74514c34a0a")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
