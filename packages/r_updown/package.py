# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpdown(RPackage):
	"""Detecting Group Disturbances from Longitudinal Observations

	Provides an algorithm to detect and characterize disturbances (start, end dates, intensity) that can occur at different hierarchical levels by studying the dynamics of longitudinal observations at the unit level and group level based on Nadaraya-Watson's smoothing curves, but also a shiny app which allows to visualize the observations and the detected disturbances. Finally the package provides a dataframe mimicking a pig farming system subsected to disturbances simulated according to Le et al.(2022) <doi:10.1016/j.animal.2022.100496>. 
	"""
	
	cran = "UpDown" 

	version("1.2.1", md5="164b00a337426614ebcccbb4defa62db")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
