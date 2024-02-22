# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcan(RPackage):
	"""Cancer Registry Data Analysis and Visualisation

	Tools for basic and advance cancer statistics and graphics.
	Groups individual data, merges registry data and population data, calculates age-specific rate, age-standardized rate, cumulative risk, estimated annual percentage rate with standards error. Creates graphics across variable and
    time, such as age-specific trends, bar chart and period-cohort trends.
	"""
	
	homepage = "https://github.com/timat35/Rcan"
	cran = "Rcan" 

	version("1.3.82", md5="3199253a80110da84a47aecc095e2659")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
