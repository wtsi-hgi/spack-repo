# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhpsurvey(RPackage):
	"""Analytic Hierarchy Process for Survey Data

	The Analytic Hierarchy Process is a versatile multi-criteria decision-making tool introduced by Saaty (1987) <doi:10.1016/0270-0255(87)90473-8> that allows decision-makers to weigh attributes and evaluate alternatives presented to them.    This package provides a consistent methodology for researchers to reformat data and run analytic hierarchy process in R on data that are formatted using the survey data entry mode. It is optimized for performing the analytic hierarchy process with many decision-makers, and provides tools and options for researchers to aggregate individual preferences and test multiple options. It also allows researchers to quantify, visualize and correct for inconsistency in the decision-maker's comparisons.
	"""
	
	cran = "ahpsurvey" 

	version("0.4.1", md5="5a2220cd433d05fca5e835aea4bf4ad7")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-randomnames", type=("build", "run"))
