# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuncharter(RPackage):
	"""Automatically Plot, Analyse and Revises Limits of Multiple Run
Charts

	Plots multiple run charts, finds successive signals of 
    improvement, and revises medians when each signal occurs. Finds runs
    above, below, or on both sides of the median, and returns a plot and
    a data.table summarising original medians and any revisions, for all
    groups within the supplied data.
	"""
	
	homepage = "https://github.com/johnmackintosh/runcharter"
	cran = "runcharter" 

	version("0.2.0", md5="50ea8c95908fb9bd1dcab8680866d0cb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
