# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAggregater(RPackage):
	"""Aggregate Numeric, Date and Categorical Variables

	Convenience functions for aggregating a data frame or data table.
    Currently mean, sum and variance are supported. For Date variables, the recency
    and duration are supported. There is also support for dummy variables in
    predictive contexts. Code has been completely re-written in data.table for computational speed. 
	"""
	
	cran = "AggregateR" 

	version("0.1.1", md5="68d972090170aa686ba4b4123e8e28c8")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ncmisc", type=("build", "run"))
