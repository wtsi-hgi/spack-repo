# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedi(RPackage):
	"""Robust Exponential Decreasing Index

	Implementation of the Robust Exponential Decreasing Index (REDI),
    proposed in the article by Issa Moussa, Arthur Leroy et al. (2019)
    <https://bmjopensem.bmj.com/content/bmjosem/5/1/e000573.full.pdf>.
    The REDI represents a measure of cumulated workload, robust to missing data,
    providing control of the decreasing influence of workload over time. 
    Various functions are provided to format data, compute REDI, and 
    visualise results in a simple and convenient way. 
	"""
	
	cran = "REDI" 

	version("1.0.0", md5="050a9c5c527669797058b75d3776e1bf")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
