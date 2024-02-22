# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbanalysis(RPackage):
	"""Multiblock Exploratory and Predictive Data Analysis

	Exploratory and predictive methods for the analysis of several blocks of variables measured on the same individuals.
	"""
	
	cran = "MBAnalysis" 

	version("2.0.2", md5="e68b6b8d082234a370bee1c4214df337")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
