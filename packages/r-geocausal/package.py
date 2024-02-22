# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeocausal(RPackage):
	"""Causal Inference with Spatio-Temporal Data

	Spatio-temporal causal inference based on point process data. 
    You provide the raw data of locations and timings of treatment and 
    outcome events, specify counterfactual scenarios, and the package 
    estimates causal effects over specified spatial and temporal windows.
    See Papadogeorgou, et  al. (2022) <doi:10.1111/rssb.12548>.
	"""
	
	homepage = "https://github.com/mmukaigawara/geocausal"
	cran = "geocausal" 

	version("0.2.0", md5="2e9b2142b73fd1bf98b8973d9ddf486a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-model", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
