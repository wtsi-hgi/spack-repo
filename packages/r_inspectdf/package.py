# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInspectdf(RPackage):
	"""Inspection, Comparison and Visualisation of Data Frames

	A collection of utilities for columnwise summary, comparison and visualisation of data frames.  Functions report missingness, categorical levels, numeric distribution, correlation, column types and memory usage.
	"""
	
	homepage = "https://alastairrushworth.github.io/inspectdf/"
	cran = "inspectdf" 

	version("0.0.12", md5="818c57b4de16c535ddf7c995e6ff0cbb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggfittext", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
