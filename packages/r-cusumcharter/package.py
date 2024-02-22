# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCusumcharter(RPackage):
	"""Easier CUSUM Control Charts

	Create CUSUM (cumulative sum) statistics from a vector or dataframe.
    Also create single or faceted CUSUM control charts, with or without control limits.
    Accepts vector, dataframe, tibble or data.table inputs.
	"""
	
	homepage = "https://github.com/johnmackintosh/cusumcharter"
	cran = "cusumcharter" 

	version("0.1.0", md5="bd480eb2150b893999ceb6ac3f971506")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
