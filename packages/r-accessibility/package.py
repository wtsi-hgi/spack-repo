# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAccessibility(RPackage):
	"""Transport Accessibility Measures

	A set of fast and convenient functions to calculate multiple
    transport accessibility measures. Given a pre-computed travel cost
    matrix and a land use dataset (containing the location of jobs,
    healthcare and population, for example), the package allows one to
    calculate active and passive accessibility levels using multiple
    accessibility measures, such as: cumulative opportunities (using
    either travel cost cutoffs or intervals), minimum travel cost to
    closest N number of activities, gravity-based (with different decay
    functions) and different floating catchment area methods.
	"""
	
	homepage = "https://github.com/ipeaGIT/accessibility"
	cran = "accessibility" 

	version("1.3.0", md5="533902d9d34adb930b0f1f39134135d3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
