# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtables(RPackage):
	"""Reporting Tables

	Reporting tables often have structure that goes beyond simple
    rectangular data. The 'rtables' package provides a framework for
    declaring complex multi-level tabulations and then applying them to
    data. This framework models both tabulation and the resulting tables
    as hierarchical, tree-like objects which support sibling sub-tables,
    arbitrary splitting or grouping of data in row and column dimensions,
    cells containing multiple values, and the concept of contextual
    summary computations. A convenient pipe-able interface is provided for
    declaring table layouts and the corresponding computations, and then
    applying them to data.
	"""
	
	homepage = "https://github.com/insightsengineering/rtables"
	cran = "rtables" 

	version("0.6.6", md5="48358c3cc4714bf389382b5405f750fe")

	depends_on("r-formatters@0.5.5:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-htmltools@0.5.4:", type=("build", "run"))
	depends_on("r-stringi@1.6:", type=("build", "run"))
