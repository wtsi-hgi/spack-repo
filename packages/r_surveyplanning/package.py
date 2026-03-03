# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurveyplanning(RPackage):
	"""Survey Planning Tools

	Tools for sample survey planning, including sample size calculation, estimation of expected precision for the estimates of totals, and calculation of optimal sample size allocation.
	"""
	
	homepage = "https://csblatvia.github.io/surveyplanning/"
	cran = "surveyplanning" 

	version("4.0", md5="c295fbb9cd03611deb9081fa1bf4bc22")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table@1.11.4:", type=("build", "run"))
	depends_on("r-laeken", type=("build", "run"))
