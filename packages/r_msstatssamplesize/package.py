# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatssamplesize(RPackage):
	"""Simulation tool for optimal design of high-dimensional MS-based proteomics experiment

	The packages estimates the variance in the input protein abundance data and simulates data with predefined number of biological replicates based on the variance estimation. It reports the mean predictive accuracy of the classifier and mean protein importance over multiple iterations of the simulation.
	"""
	
	homepage = "http://msstats.org"
	bioc = "MSstatsSampleSize" 

	version("1.16.0", commit="c984b876f3d704186c0876495e81cdc385310fe1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-msstats", type=("build", "run"))
