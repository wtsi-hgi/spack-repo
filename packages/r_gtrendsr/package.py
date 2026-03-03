# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtrendsr(RPackage):
	"""Perform and Display Google Trends Queries

	An interface for retrieving and displaying the information
        returned online by Google Trends is provided. Trends (number of
        hits) over the time as well as geographic representation of the
        results can be displayed.
	"""
	
	homepage = "https://github.com/PMassicotte/gtrendsR"
	cran = "gtrendsR" 

	version("1.5.1", md5="153b2a85a01070aca55e6e72e3edba45")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
