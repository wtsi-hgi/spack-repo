# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSampler(RPackage):
	"""Sample Design, Drawing & Data Analysis Using Data Frames

	Determine sample sizes, draw samples, and conduct data analysis using data frames. It specifically enables you to determine simple random sample sizes, stratified sample sizes, and complex stratified sample sizes using a secondary variable such as population; draw simple random samples and stratified random samples from sampling data frames; determine which observations are missing from a random sample, missing by strata, duplicated within a dataset; and perform data analysis, including proportions, margins of error and upper and lower bounds for simple, stratified and cluster sample designs. 
	"""
	
	homepage = "https://github.com/mbaldassaro/sampler"
	cran = "sampler" 

	version("0.2.4", md5="33c389a7d6f52b793516be30bd60136f")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
